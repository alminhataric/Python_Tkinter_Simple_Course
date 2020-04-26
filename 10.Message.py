from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title = ("Welcome to Python")




def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello world!")
    Label(root, text=response).pack()
    #if response == "yes":
     #   Label(root, text="You clicked yes!").pack()
    #else:
     #   Label(root, text="You clicked no!").pack()


Button(root, text="Popup", command=popup).pack()














mainloop()