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
complete = False
Score = 0
Question = 0
List = []
while complete == False:
    Add1 = random.randint(1, 10)
    Add2 = random.randint(1, 10)
    Ans1 = Add1 + Add2
    List.append(Ans1)
    Ques1 = simpledialog.askinteger("Question", "What is {} + {} ".format(Add1, Add2))
    if Question == 10:
        messagebox.showinfo("Game Over", "Game Over, Your Score Was {}".format(Score))
        List = []
        complete = True
    elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            Question += 1
            List = []
            print (Question)
            print(Score)


    else:
        messagebox.showerror("WRONG", "Incorrect")
        Question += 1
        print(Question)
        print(Score)
        List = []


nutt = tk.Button(text="Home", command=go_home)
nutt.pack()

def go_home():
    import main
    main


nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
