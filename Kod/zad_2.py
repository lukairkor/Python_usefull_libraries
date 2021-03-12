import numpy as np
import cv2

img = cv2.imread('lena.png')

cv2.rectangle(img,(210,210),(360,400),(0,0,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Labolatorium SK',(305,500), font, 0.75,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()