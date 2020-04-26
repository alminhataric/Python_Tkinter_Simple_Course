from tkinter import *
from PIL import ImageTk, Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title = ("Welcome to Python")

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in MODES:
    Radiobutton(root,text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command= lambda:clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()


myButton=Button(root,text="Clicked me",command= lambda:clicked(pizza.get())).pack()







mainloop()
