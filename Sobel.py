import cv2 
import numpy as np 
image=cv2.imread(r"E:\cv lab\bike.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_gauss=cv2.GaussianBlur(gray,(3,3),0)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = np.sqrt(sobel_x ** 2 + sobel_y ** 2).astype(np.uint8)
cv2.imshow("Output_Sobel",sobel_edges)
cv2.waitKey(0)