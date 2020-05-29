import cv2
import numpy as np
from PIL import Image
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(1);
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("dataset/train_fac.yml")
id=0
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

def getProfile(i):
    conn=sqlite3.connect("person.db")
    cmd="Select * from per WHERE id ="+str(i)
    cursor=conn.execute(cmd)
    Profile=None
    for row in cursor:
        Profile=row
    conn.execute(cmd)
    conn.commit()
    conn.close()
    return Profile

while(True):
    ret,im=cam.read();
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
        text=cv2.putText(im, "Number of faces detected: " + str(faces.shape[0]), (0, im.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), 1)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            for i in range(15):
                if(id==i):
                    Profile=getProfile(i)
                    print(Profile)
                    if(Profile!=None):
                        cv2.putText(im, str(Profile[1]), (x,y+h+20), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(im, str(Profile[2]), (x,y+h+40), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(im, str(Profile[3]), (x,y+h+60), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), 1)
                    
                else: 
                    if(i<15):
                        continue
                    else:
                        id="Unknown"
        cv2.putText(im,str(id),(x,y+h),font,2,(255,0,0),3);
    cv2.imshow("im",im);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
