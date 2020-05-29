from tkinter import *
import os
import cv2
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id = 0;

x = (input("Cam ready to capture photo 1.Yes 2.NO :"))

if x == "1":
    print("name of the folder")
    nameFolder = input()
    os.chdir('F:\\open\\opencv\\untitled\\photo')
    os.mkdir("" + nameFolder)
    os.chdir("" + nameFolder)

id = input("enter your id :")

file = askopenfilename()

image = cv2.imread(file)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grayImage)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    cv2.rectangle(image, ((0, image.shape[0] - 25)), (270, image.shape[0]), (255, 255, 255), -1)
    cv2.imwrite("User."+str(id)+".jpg", grayImage[y:y + h, x:x + w])

cv2.waitKey(0)
cv2.destroyAllWindows()