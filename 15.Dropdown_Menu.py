from tkinter import *
from PIL import ImageTk, Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()



option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thrusday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(option[0])

drop = OptionMenu(root, clicked, *option)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()