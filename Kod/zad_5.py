import numpy as np
import cv2

img = cv2.imread('lena.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 

cv2.rectangle(img,(210,210),(360,400),(0,0,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Labolatorium SK',(305,500), font, 0.75,(255,255,255),2,cv2.LINE_AA)

y=210
x=210
h=400-210
w=360-210

crop = img[y:y+h, x:x+w]

cv2.imshow("cropped", crop)
cv2.imwrite('lena_grey_template.png',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()