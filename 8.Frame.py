from tkinter import  *
from PIL import  ImageTk,Image

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")

frame =  LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Dont click here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)




root.mainloop()