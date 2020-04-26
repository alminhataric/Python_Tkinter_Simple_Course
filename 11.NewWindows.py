from tkinter import *
from PIL import ImageTk,Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root =Tk()
root.title("Welcome to Python")


def open():
    global my_img
    top = Toplevel()
    top.title("Python rules")
    my_img = ImageTk.PhotoImage(Image.open("Path of image"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close windows", command=top.destroy).pack()


btn = Button(root, text = "Open second window", command=open).pack()


mainloop()