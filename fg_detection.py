# import required libraries
import numpy as np
import cv2

# from matplotlib import pyplot as plt

# read input image
img = cv2.imread(r'E:\cv lab\face.jpg')
cv2.imshow("original image",img)

# define mask
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# define rectangle
rect = (150,50,500,500)

# apply grabCut method to extract the foreground
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,20,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

# display the extracted foreground image

# plt.imshow(img),plt.colorbar(),plt.show()
cv2.imshow('Foreground Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()