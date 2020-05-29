from tkinter import *
import os
import cv2
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import numpy as np


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
file = askopenfilename()
img = cv2.imread(file)

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("photo/train_img.yml")
id=0
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
while(True):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(id==1):
                id="Altaf"
            elif(id==2):
                id="kal"
            elif(id==3):
                id="kishore"
        else:
            id="Unknown"
        cv2.putText(img,str(id),(x,y+h),font,5,(255,0,0),3);
    cv2.imshow("img",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cv2.destroyAllWindows()
