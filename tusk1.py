from tkinter import ttk
import tkinter as tk
def label():
    label = ttk.Label(text ="Hello word!")
    label.pack()
room = tk.Tk()
a = ttk.Button(text = "кнопка", command = label)
a.pack()
room.mainloop()
