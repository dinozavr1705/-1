from tkinter import ttk
import tkinter as tk
class Calculator:
    def __init__(self):
      self.bruh=""
    def plus(self):
        a1 = a.get()
        b1 = b.get()
        self.bruh = self.bruh + f"{a1} + {b1} "

    def minus(self):
        a1 = int(a.get())
        b1 = int(b.get())
        self.bruh = self.bruh + f"{a1} - {b1} "
    def equal(self):
        self.label =ttk.Label(text =f"{eval(self.bruh)}")
        self.label.pack()
        self.bruh =""
calcul = Calculator()
room = tk.Tk()
a = ttk.Entry()
a.pack()
b = ttk.Entry()
b.pack()
plus_button = ttk.Button(text = "+",command = calcul.plus)
plus_button.pack()
minus_button = ttk.Button(text ="-",command = calcul.minus)
minus_button.pack()
equal_button = ttk.Button(text ="=",command = calcul.equal)
equal_button.pack()

room.mainloop()
