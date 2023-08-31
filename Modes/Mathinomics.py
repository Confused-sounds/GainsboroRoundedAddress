import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

windr = tk.Tk()
windr.title("EX")
windr.geometry("300x300")
messagebox.showinfo(
    "GOW",
    "EX Mode Selected",
)


def go_home():
    import main
    main


nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
