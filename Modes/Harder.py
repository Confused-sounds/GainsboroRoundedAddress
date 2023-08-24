import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk


global Beat_mode
Beat_mode = True
windr = tk.Tk()
windr.title("Hard")
windr.geometry("300x300")
messagebox.showinfo(
    "Herd",
    "Hard Mode Selected",
)
def go_home():
    windr.destroy()
    import main
    main

    
    
    
    

nutt = tk.Button(text="Home", command=go_home)
nutt.pack()