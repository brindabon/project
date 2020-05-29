from tkinter import *
import os

root = Tk()

root.configure(background="blue")
root.title("DETECTION")
root.canvas = Canvas(root, width=600, height=500, bg="blue")
root.canvas.pack(expand=YES, fill=BOTH)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x = int(width / 2 - 600 / 2)
y = int(height / 2 - 500 / 2)
str1 = "600x500+" + str(x) + "+" + str(y)
root.geometry(str1)

# disable resize of the window
root.resizable(width=False, height=False)
root.frame = Frame(root, height=400, width=450)
root.frame.place(x=80, y=50)

x, y = 70, 20

root.img = PhotoImage(file='image\\login.png')
root.label = Label(root.frame, image=root.img)
root.label.place(x=0, y=0)
email = ()


def cam():
    os.system("py cam.py")

def img():
    os.system("py img_detect.py")


def back():
    root.destroy()
    #os.system("py uitry.py")


root.label = Label(root.frame, text="SELECT YOUR OPTION")
root.label.config(font=("Courier", 20, 'bold'))
root.label.place(x=70, y=y + 120)

root.button = Button(root.frame, text="FACE DETECTION IN REAL TIME", font='Courier 15 bold', bg="red", command=cam)
root.button.place(x=50, y=y + 200)

root.button = Button(root.frame, text="FACE DETECTION IN IMAGE", font='Courier 15 bold', bg="red", command=img)
root.button.place(x=70, y=y + 270)

root.button = Button(root.frame, text="BACK", font='Courier 15 bold', bg="red",command=back)
root.button.place(x=170, y=y+350)

root.mainloop()