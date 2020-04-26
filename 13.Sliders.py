from tkinter import *
from PIL import ImageTk, Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")
root.geometry("400x400")


vertical = Scale(root, from_=0, to=400)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))



horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()



my_btn = Button(root,text="Click me", command=slide).pack()



mainloop()