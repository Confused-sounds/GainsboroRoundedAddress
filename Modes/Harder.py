import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

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


global Beat_mode
Beat_mode = None

while Beat_mode == None:
    Beat_mode = True
    try:
        if Beat_mode == True:
            messagebox.showinfo("POGCHAMP!!!!!",
                                "'I Am No Mere Child' Difficulty Unlocked!")
    except:
        if Beat_mode == None:
            break

nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
