from tkinter import *
from PIL import ImageTk, Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")
root.geometry("400x400")

var = StringVar()

def show():
    myLabel = Label(root, text=var.get()).pack()


c = Checkbutton(root, text="Check this box ,I dare you", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Show selection", command=show).pack()





root.mainloop()