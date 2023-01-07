import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
    for (x,y,w,h) in faces:
        
        crop = img[y:y+h, x:x+w]
        rotated=cv2.rotate(crop, cv2.ROTATE_180)
        
        cv2.rectangle(rotated,(x,y),(x+w,y+h),(0,0,255),2)

        
    cv2.imshow('img',rotated)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

