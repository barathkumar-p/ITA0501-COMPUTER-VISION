import cv2
import numpy as np
path=r"E:\cv lab\car.jpg"
img=cv2.imread(path)
cv2.imshow(img)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Graysclae",imgGray)
cv2.waitKey(0)