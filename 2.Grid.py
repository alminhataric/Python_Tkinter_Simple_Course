from tkinter import *

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="I'm Batman")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()