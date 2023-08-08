import cv2
path=r"E:\cv lab\bike.jpg"
src = cv2.imread(path)
cv2.imshow("original image",src)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)