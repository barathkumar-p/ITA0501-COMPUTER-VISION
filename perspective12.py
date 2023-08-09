from importlib.resources import path
from turtle import width
import cv2
import numpy as np
path=r"E:\cv lab\bike.jpg"
img = cv2.imread(path)
rows,cols,ch=img.shape
pts1 = np.float32([[50,50],[400,95],[45,238],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow("transform image",dst)
cv2.waitKey(0)
