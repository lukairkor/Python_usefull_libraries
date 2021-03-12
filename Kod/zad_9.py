import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        

        for (ex,ey,ew,eh) in eyes:
            aaa=cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            c0 = int((ex+ey)/2)
            c1 = int((ew+eh)/2)
            # print('Ball centre: {},{}'.format(c0,c1))
            ca = str(c0)
            cb = str(c1)
            xxxx = ca+' '+cb
            # print(eyes.shape)
            if eyes.shape ==  (2,4):
                if ex in eyes[1,:]:
                    cv2.putText(img,xxxx,(400,150), font, 0.75,(0,255,255),2,cv2.LINE_AA)
                    
                if ex in eyes[0,:]:
                    cv2.putText(img,xxxx,(250,150), font, 0.75,(0,255,255),2,cv2.LINE_AA)
            else:
                break
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()