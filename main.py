import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Diff select")
window.geometry("300x300")


def Nuh_uh():
    image = Image.open("NUH_UH.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.pack()
    button.config(state=tk.DISABLED)
    messagebox.showerror('NUH UH', 'Complete Hard mode to unlock')
    window.mainloop()


def Ezmody():
    window.destroy()
    import Modes 
    from Modes import Ezmod
    Modes
    Ezmod


hello = tk.Label(text="Select Diff")
hello.place(relx=.5, rely=.7)
hello.pack()
button = tk.Button(text="I am no mere child", command=Nuh_uh)
button.pack()
butt2 = tk.Button(text="Hard")
butt2.pack()
butt3 = tk.Button(text="Normal")
butt3.pack()
butt4 = tk.Button(text="Easy", command=Ezmody)
butt4.pack()

tk.mainloop()
