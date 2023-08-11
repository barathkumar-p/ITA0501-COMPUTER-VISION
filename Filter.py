import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path=r"E:\cv lab\bike.jpg"
image=cv.imread(path)
kernel1=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
filter1=cv.filter2D(src=image,ddepth=-1,kernel=kernel1)
cv.imshow("Output",filter1)
cv.waitKey(0)