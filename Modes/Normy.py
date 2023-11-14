import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

windr = tk.Tk()
windr.title("Normal")
windr.geometry("300x300")
messagebox.showinfo(
    "Mid",
    "Normal Mode Selected",
)

swap = False
def go_home():
    windr.destroy()
    import main
    main


complete = False
Score = 0
Question = 0
List = []
while complete == False:
    Add1 = random.randint(10, 20)
    Add2 = random.randint(10, 20)
    Thingy = random.randint(1, 2)
    print(Thingy)
    if Thingy == 1:
        Ans1 = Add1 + Add2
        List.append(Ans1)
        Ques1 = simpledialog.askinteger("Question {}, Score {}/10".format(Question,Score),
                                        "What is {} + {} ".format(Add1, Add2))
        if Question == 10:
            messagebox.showinfo("Game Over",
                                "Game Over, Your Score Was {}".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            Question += 1
            List = []
            print(Question)
            print(Score)

        else:
            messagebox.showerror("WRONG", "Incorrect")
            Question += 1
            print(Question)
            print(Score)
            List = []

    else:
        if Add2 > Add1: 
            Ans2 = Add2 - Add1
        elif Add1 > Add2:
            Ans2 = Add1 - Add2
            swap = True
        else:
            print ("err")
            break
        List.append(Ans2)
        if swap == True:
            Ques1 = simpledialog.askinteger("Question {}, Score {}/10".format(Question, Score),
                                        "What is {} - {} ".format(Add1, Add2))
        else:
            Ques1 = simpledialog.askinteger("Question {}, Score {}/10".format(Question, Score),
                                        "What is {} - {} ".format(Add2, Add1))
        if Question == 10:
            messagebox.showinfo("Game Over",
                                "Game Over, Your Score Was {}".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            Question += 1
            List = []
            print(Question)
            print(Score)

        else:
            messagebox.showerror("WRONG", "Incorrect")
            Question += 1
            print(Question)
            print(Score)
            List = []

nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
