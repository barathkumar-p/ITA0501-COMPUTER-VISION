import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
path=r"E:\cv lab\bike.jpg"
img = cv2.imread(path,cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
