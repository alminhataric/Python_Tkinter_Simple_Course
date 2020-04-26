from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="Path of the file", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

mainloop()