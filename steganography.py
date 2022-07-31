from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

# Create interface
root = Tk()
root.title("Steganography - Hide a text message in an image")
root.geometry("900x700+250+50")
root.resizable(False,False)
root.configure(bg="#4a4a4a")
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)
logo = PhotoImage(file="logo.png")
logo = logo.zoom(25)
logo = logo.subsample(30)
Label(root,image=logo,bg="#4a4a4a").place(x=20,y=0)

Label(root,text="Fanny's Steganography tool",bg="#4a4a4a",fg="white",font="arial 25 bold").place(x=250,y=50)

# First frame
frame1 = Frame(root,bd = 3,bg="black",width=400,height=350,relief=GROOVE)
frame1.place(x=50,y=200)

lbl=Label(frame1,bg="black")
lbl.place(x=20,y=50)

# Second frame
frame2 = Frame(root,bd = 3,bg="white",width=400,height=350,relief=GROOVE)
frame2.place(x=450,y=200)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=380,height=330)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=400,y=0,height=500)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


def showImage():
    global filename
    filename = filedialog.askopenfile(initialdir=os.getcwd()
                                      ,title="Select Image File"
                                      ,filetype=(("PNG file","*.png"),
                                                 ("JPG file","*.jpg")
                                                 ,("All file","*.txt")))
    image = Image.open(filename.name)
    image = ImageTk.PhotoImage(image)
    lbl.configure(image=image,width=350,height=250)
    lbl.image = image

def hide():
    global secret
    message = text1.get(1.0,END)
    secret = lsb.hide(str(filename.name),message)

def show():
    clearMessage = lsb.reveal(filename.name)
    text1.delete(1.0,END)
    text1.insert(END,clearMessage)

def save():
    secret.save("hidden.png")

# Third frame
frame3 = Frame(root,bd = 3,bg="#4a4a4a",width=400,height=100,relief=GROOVE)
frame3.place(x=50,y=560)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showImage).place(x=40,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=240,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#4a4a4a",fg="white").place(x=120,y=5)

# Fourth frame
frame4 = Frame(root,bd = 3,bg="#4a4a4a",width=400,height=100,relief=GROOVE)
frame4.place(x=450,y=560)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=hide).place(x=40,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=show).place(x=240,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#4a4a4a",fg="white").place(x=120,y=5)

root.mainloop()
