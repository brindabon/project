import numpy as np
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
file = askopenfilename()
image = cv2.imread(file)

while True:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        text=cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0, image.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Face',image)
    if(cv2.waitKey(1)==ord('q')):
        break;

cv2.destroyAllWindows()
