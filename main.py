import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Gam")
window.geometry("300x300")
   

def clack():
    image = Image.open("MicrosoftTeams-image (1).png") 
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.pack()
    window.mainloop()
    
hello = tk.Label(text="Main Menu")
hello.place(relx = .5, rely = .7, anchor="n",)
hello.pack()
button = tk.Button(text="Yes",
                   command=clack)
button.place(relx = .5, rely = .9, anchor="center")
button.pack()

    








tk.mainloop()
