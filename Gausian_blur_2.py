import cv2
import numpy as np
path=r"E:\cv lab\car1.jpg"
img=cv2.imread(path)
i=cv2.resize(img,(720,720))
cv2.imshow("org img",i)
#imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("img Blur",imgBlur)
cv2.waitKey(0)
