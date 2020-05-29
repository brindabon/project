import cv2
import sqlite3
import numpy as np
import os

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(1)
rec=cv2.face.LBPHFaceRecognizer_create()

def insertOrUpdate(id,name):
    conn=sqlite3.connect("person.db")
    cmd="Select * from per WHERE id ="+str(id)
    cursor = conn.execute(cmd)
    isRecorderExist=0
    for row in cursor:
        isRecorderExist=1
    if(isRecorderExist==1):
        cmd="UPDATE per SET name="+str(name)+"where id ="+str(id)
    else:
        cmd="INSERT INTO per (id,name) values("+str(id)+","+str(name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
photo = "1"

x = (input("Cam ready to capture photo 1.Yes 2.NO :"))

if x == "1":
    print("name of the folder")
    nameFolder = input()
    os.chdir('F:\\open\\opencv\\untitled\\dataset')
    os.mkdir(""+nameFolder)
    os.chdir(""+nameFolder)
    
id = input("enter your id :")
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(200);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20):
        break
    
os.chdir('F:\\open\\opencv\\ana')
name = input('enter your name :')
insertOrUpdate(id,name)
cam.release()
cv2.destroyAllWindows()
