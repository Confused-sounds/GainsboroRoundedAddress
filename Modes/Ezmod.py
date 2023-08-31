import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

windr = tk.Tk()
windr.title("Easy")
windr.geometry("300x300")
messagebox.showinfo(
    "EZ",
    "Easy Mode Selected",
)


def go_home():
    windr.destroy()
    import main
    main


nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
