#import module from tkinter for UI
from tkinter import *
import os
import cv2
#creating instance of TK
root=Tk()


def function1():
    os.system("py ask_detect.py")
       
def function2():
    os.system("py ask_store.py")

def function3():
    os.system("py ask_train.py")
    
def function4():
    os.system("py ask_rec.py")
    
def function5():
    os.system("py countface.py")

#stting title for the window
root.title("FACE RECOGNITION")
root.configure(background="blue")
root.canvas = Canvas(root, width=600, height=500, bg="blue")
root.canvas.pack(expand=YES, fill=BOTH)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x = int(width / 2 - 600 / 2)
y = int(height / 2 - 750 / 2)
str1 = "950x690+" + str(x) + "+" + str(y)
root.geometry(str1)

root.resizable(width=False, height=False)

root.img1 = PhotoImage(file='image\\banner.gif')
root.label = Label(image=root.img1, height=200, width=920)
root.label.place(x = 10, y = 70)


root.img2 = PhotoImage(file='image\\Rana.png')
root.label1 = Label(image=root.img2, height=190, width=250)
root.label1.place(x = 30, y = 460)

root.lab=Label(root, text="N. Rana Singha",font=("times new roman",15,"bold"),bg="blue",fg="white")
root.lab.place(x=80, y=650)

root.img3 = PhotoImage(file='image\\b2.png')
root.label = Label(image=root.img3, height=190, width=250)
root.label.place(x = 350, y = 460)

root.lab=Label(root, text="BRINDABON BORUAH",font=("times new roman",15,"bold"),bg="blue",fg="white")
root.lab.place(x=370, y=650)

root.img4 = PhotoImage(file='image\\a7.png')
root.label2 = Label(image=root.img4, height=190, width=250)
root.label2.place(x = 660, y = 460)

root.lab=Label(root, text="ALTAF HUSSAIN",font=("times new roman",15,"bold"),bg="blue",fg="white")
root.lab.place(x=710, y=650)
#creating a text label
root.lab=Label(root, text="FACE RECOGNITION SYSTEM",font=("times new roman",20,"bold"),bg="blue",fg="white",height=2)
root.lab.place(x=255, y=4)

root.lab=Label(root, text="OUR SERVICES",font=("times new roman",20,"bold"),bg="blue",fg="white",height=2)
root.lab.place(x=347, y=273)

root.lab=Label(root, text="OUR TEAM",font=("times new roman",20,"bold"),bg="blue",fg="white",height=2)
root.lab.place(x=370, y=387)

#creating first button
b1=Button(root,text="DETECTION",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1)
b1.place(x=15,y=335)
#creating second button
b2=Button(root,text="FACE STORE",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2)
b2.place(x=198,y=335)
#creating third button
b3=Button(root,text="TRAIN FACE",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3)
b3.place(x=390,y=335)
#creating 4th button
b4=Button(root,text="RECOGNITION",font=('times new roman',20),bg="#0D47A1",fg="white",command=function4)
b4.place(x=580,y=335)
#creating 5th button
b5=Button(root,text="SECURITY",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5)
b5.place(x=790,y=335)
#creating exit button
#b6=Button(root,text="Exit",font=('times new roman',20),bg="#0D47A1",fg="white",command=function6)
#b6.place(x=870,y=290)
root.mainloop()
