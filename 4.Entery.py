from tkinter import *

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()

e = Entry(root, width=50)
e.pack()


def myClick():
    hello = "Hello "+ e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter youre name", command=myClick)
myButton.pack()


root.mainloop()