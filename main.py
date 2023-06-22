import tkinter as tk
from tkinter import ttk
import tkinter.font
def _innit_():
    Menu = tk.Tk()
    Menu.title("Gam")
    Menu.geometry("723x373")


    hello = ttk.Label(text="Main Menu")
    Desired_font = tkinter.font.Font(family = "Comic Sans MS", size = 10)
    hello.place(relx = .5, rely = .1, anchor="n",)
    hello.configure(font = Desired_font)
    
    button = ttk.Button(text="Settings")
    button.place(relx = .5, rely = .5, anchor="center")










_innit_()
tk.mainloop()