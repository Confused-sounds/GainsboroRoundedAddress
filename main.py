import tkinter as tk
import time
from tkinter import messagebox
from PIL import Image, ImageTk
import Modes


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
    Modes
    Mathinomics


def Diff_select():
    Label.destroy()
    Buttn.destroy()
    Exit.destroy()
    global butter
    hello = tk.Label(text="Select Diff")
    hello.place(relx=.5, rely=.7)
    hello.pack()
    butter = tk.Button(text="I Am No Mere Child", command=Nuh_uh)
    butter.pack()
    butt2 = tk.Button(text="Hard", command=Hard)
    butt2.pack()
    butt3 = tk.Button(text="Normal", command=Mid)
    butt3.pack()
    butt4 = tk.Button(text="Easy", command=Ezmody)
    butt4.pack()


def Nuh_uh():
    butter.config(state=tk.DISABLED)
    image = Image.open("NUH_UH.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.pack()
    messagebox.showerror('NUH UH', 'Mode Incomplete')
    label.destroy()
    window.mainloop()




Label = tk.Label(text="MATH GAME")
Label.pack()
Buttn = tk.Button(text="Play", command=Diff_select)
Buttn.pack()
Exit = tk.Button(text="Exit", command=leaf)
Exit.pack()

tk.mainloop()
