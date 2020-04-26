from tkinter import *
from PIL import ImageTk,Image


#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

#If you want to open image you need to create folder and put images there
#So you can open them with code

my_img = ImageTk.PhotoImage(Image.open("You put image path in here"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
