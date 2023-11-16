import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog

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
    Add1 = random.randint(50, 100)
    Add2 = random.randint(50, 100)
    Thingy = random.randint(1, 3)
    if Thingy == 1:
        Ans1 = Add1 + Add2
        List.append(Ans1)
        Question += 1
        Ques1 = simpledialog.askinteger(
            "Question {}, Score {}/15".format(Question, Score),
            "What is {} + {} ".format(Add1, Add2))
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            List = []

        else:
            messagebox.showerror("WRONG", "Incorrect")
            List = []

    elif Thingy == 2:
        Ans1 = Add1 - Add2
        List.append(Ans1)
        Question += 1
        Ques1 = simpledialog.askinteger(
            "Question {}, Score {}/15".format(Question, Score),
            "What is {} - {} ".format(Add1, Add2))
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            List = []

        else:
            messagebox.showerror("WRONG", "Incorrect")
            List = []
    else:
        Add3 = random.randint(50, 100)
        Add4 = random.randint(10, 50)
        Ans1 = Add3 * Add4
        List.append(Ans1)
        Question += 1
        Ques1 = simpledialog.askinteger(
            "Question {}, Score {}/10".format(Question, Score),
            "What is {} x {} ".format(Add3, Add4))
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            List = []

        else:
            messagebox.showerror("WRONG", "Incorrect")
            List = []
#Division goes here