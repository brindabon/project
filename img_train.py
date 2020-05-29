import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create();

photo = "1"
os.chdir('F:\\open\\opencv\\untitled\\photo')
x = (input("Do you want to train folder 1.Yes 2.NO :"))

if x == "1":
    print("name of the folder")
    nameFolder = input()

path = '' + nameFolder


def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L');
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
    return IDs, faces


Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('train_img.yml')
print("Sucessfully train your image")
cv2.destroyAllWindows()
