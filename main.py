import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Gam")
window.geometry("300x300")
   

def picture():
        image = Image.open("NUH_UH.png") 
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.pack()
        button.config(state=tk.DISABLED)
        print ("Complete hard mode to unlock")
        window.mainloop()


hello = tk.Label(text="Main Menu")
hello.place(relx = .5, rely = .7, anchor="n",)
hello.pack()
button = tk.Button(text="I am no mere child",
                   command=picture)
button.place(relx = .5, rely = .9, anchor="center")
button.pack()





tk.mainloop()