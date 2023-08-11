import cv2
import numpy as np
img=cv2.imread( r"E:\cv lab\bike.jpg")

#median blur

median=cv2.medianBlur(img,5)
cv2.imshow("image",median)
cv2.waitKey(0)

#bilateral blur

bilateral=cv2.bilateralFilter(img,5,56,7)
cv2.imshow("image",bilateral)
cv2.waitKey(0)