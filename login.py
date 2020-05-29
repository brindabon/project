from tkinter import *
import os

root=Tk()

root.configure(background="blue")
root.title("LOGIN")
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
root.label.place(x = 0, y = 0)
email=()

def close():
    root.destroy()

def fun():
    if root.email.get() == "altaf":
        root.destroy()
        os.system("py uitry.py")
        
def face():
    root.destroy()
    os.system("py faceunlock.py")
    
        

root.label = Label(root.frame, text="USER LOGIN")
root.label.config(font=("Courier", 20, 'bold'))
root.label.place(x=140, y = y + 150)

root.emlabel = Label(root.frame, text="ENTER USERNAME")
root.emlabel.config(font=("Courier", 12, 'bold'))
root.emlabel.place(x=50, y= y + 230)

root.email = Entry(root.frame, font='Courier 12')
root.email.place(x=200, y= y + 230)

root.pslabel = Label(root.frame, text="ENTER PASSWORD")
root.pslabel.config(font=("Courier", 12, 'bold'))
root.pslabel.place(x=50, y=y+260)

root.password = Entry(root.frame,show='*', font='Courier 12')
root.password.place(x=200, y=y+260)

root.button = Button(root.frame, text="LOGIN", font='Courier 15 bold', bg="red",command=fun)                            
root.button.place(x=170, y=y+300)

#root.button = Button(root.frame, text="FACE UNLOCK", font='Courier 15 bold', bg="red",command=face)                            
#root.button.place(x=130, y=y+350)

root.mainloop()