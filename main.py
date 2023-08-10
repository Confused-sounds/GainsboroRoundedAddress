import tkinter as tk
import time
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Gam")
window.geometry("300x300")


def leaf():
    Label.destroy()
    Exit.destroy()
    Buttn.destroy()
    messagebox.showinfo('Closing', 'ight')
    time.sleep(2)
    exit()


def Ezmody():
    window.destroy()
    import Modes
    from Modes import Ezmod
    Modes
    Ezmod


def Mid():
    window.destroy()
    import Modes
    from Modes import Normy
    Modes
    Normy


def Hard():
    window.destroy()
    import Modes
    from Modes import Harder
    Modes
    Harder


def NOMERECHILD():
    window.destroy()
    import Modes
    from Modes import Mathinomics
    Modes
    Mathinomics


def Diff_select():
    Label.destroy()
    Buttn.destroy()
    Exit.destroy()
    hello = tk.Label(text="Select Diff")
    hello.place(relx=.5, rely=.7)
    hello.pack()
    butter = tk.Button(text="I am no mere child", command=Nuh_uh)
    butter.pack()
    butt2 = tk.Button(text="Hard", command=Hard)
    butt2.pack()
    butt3 = tk.Button(text="Normal", command=Mid)
    butt3.pack()
    butt4 = tk.Button(text="Easy", command=Ezmody)
    butt4.pack()


def Nuh_uh():
    image = Image.open("NUH_UH.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.pack()
    butter.config(state=tk.DISABLED)
    messagebox.showerror('NUH UH', 'Complete Hard mode to unlock')
    window.mainloop()


Label = tk.Label(text="MATH GAME")
Label.pack()
Buttn = tk.Button(text="Play", command=Diff_select)
Buttn.pack()
Exit = tk.Button(text="Exit", command=leaf)
Exit.pack()

tk.mainloop()
