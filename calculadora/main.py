#!/usr/bin/python3


import tkinter as tk
from tkinter import messagebox


# Creacion de la ventana principal
root = tk.Tk()
# Titulo de la ventana
root.title("Calculadora")
# Size
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')


class Calculadora:

    def __init__(self, ventana) -> None:
        self.ventana = ventana

        # Representacion del display
        self.display = tk.Entry(ventana, width=15, font=('Arial', 23), bd=6,insertwidth=1, bg="#6495DE", fg="black", justify="right") # Con una linea nos vale, no hace falta usar tk.Text()
        #self.display.focus()
        self.display.grid(row=0, column=0, columnspan=4, pady=5, padx=15)


        self.current = ''
        self.op_verification = False # Chivato que me va a decir cuando pulso una operacion
        self.op = '' # Para almacenar la operacion
        self.total = 0



        row = 1
        col = 0

        # represento los botones
        buttons = [
            "7" , "8", "9", "/",
            "4" , "5", "6", "*",
            "1" , "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1 # Incremento la columna
            if col > 3:
                col = 0
                row += 1


        self.ventana.bind("<Key>", self.key_press)


    def key_press(self, event):
        key = event.char


        if key == "\r":
            print(f"\n[+] Se ha presionado la tecla Enter.")
            self.calculate()
        if key == "\x08":
            print(f"\n[+] Se ha presionado la tecla Backspace.")
            # Deberia borrarme el ultimo numero del display
            txt = self.display.get()[:-1] # Cojo todo menos el ultimo caracter
            self.display.delete(0,tk.END)
            self.display.insert(0, txt)
        if key == "\x1b":
            print(f"\n[+] Se ha presionado la tecla Escape.")
            r = messagebox.askyesno("Salir", "Estas seguro de que deseas salir de la aplicacion?")

            if r:
                self.ventana.destroy()
        if key in "0123456789+-?.*":
            self.click(key)
        
            




    def build_button(self, button_text:str, row:int, col:int):
        if button_text == "C":
            b = tk.Button(self.ventana, text=button_text, width=6, font=('Arial', 9), command=lambda: self.clear_display())
        elif button_text == "=":
            b = tk.Button(self.ventana, text=button_text, width=6, font=('Arial', 9), command=lambda: self.calculate())
        else:
            b = tk.Button(self.ventana, text=button_text, width=6, font=('Arial', 9), command=lambda: self.click(button_text)) #! Si usamos la sintaxis de LAMBDA podemos pasarle parametros a la func sin llamarla
        
        b.grid(row=row, column=col)

    def clear_display(self):
        self.display.delete(0, tk.END) # Con el widget tk.Text() seria .delete("1.0", tk.END)
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0


    def calculate(self):
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)
        
        self.display.delete(0,tk.END)
        if self.total.is_integer():
            self.total = int(self.total)
        self.display.insert(tk.END, round(self.total, 3))

    def click(self, button_text):


        if self.op_verification:
            self.op_verification = False
        
        self.display.insert(tk.END, button_text)
        
        

        if button_text in "0123456789" or button_text == ".":
            self.current += button_text

        else: # Si entramos aqui es porque le he dado a alguna operacion
            if self.current:
                if not self.op:
                    self.total = float(self.current)
            
            
            self.current = ''
            self.op_verification = True
            self.op = button_text
        
        
















my_gui = Calculadora(root)

root.mainloop()