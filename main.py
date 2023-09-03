import tkinter as tk
import time
from tkinter import messagebox
from PIL import Image, ImageTk
import Modes

window = tk.Tk()
window.title("Gam")
window.geometry("300x300")
global butter


def leaf():
    Label.destroy()
    Exit.destroy()
    Buttn.destroy()
    Global.destroy()
    messagebox.showinfo('Closing', 'ight')
    time.sleep(2)
    exit()


def Ezmody():
    window.destroy()
    from Modes import Ezmod
    Modes
    Ezmod


def Mid():
    window.destroy()
    from Modes import Normy
    Modes
    Normy


def Hard():
    window.destroy()
    from Modes import Harder
    Modes
    Harder


def NOMERECHILD():
    window.destroy()
    from Modes import Mathinomics
    Modes+


def Nuh_uh():
    butter.config(state=tk.DISABLED)
    image = Image.open("NUH_UH.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.pack()
    messagebox.showerror('NUH UH', 'Complete Hard mode to unlock')
    window.mainloop()


def globald():
    while Beat_mode == True:
        print("IT LIIIIIIIVES!!!!!!!!!!!")
        break


Label = tk.Label(text="MATH GAME")
Label.pack()
Buttn = tk.Button(text="Play", command=Diff_select)
Buttn.pack()
Exit = tk.Button(text="Exit", command=leaf)
Exit.pack()
Global = tk.Button(text="Global", command=globald)
Global.pack()

tk.mainloop()
