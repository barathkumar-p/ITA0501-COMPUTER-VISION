import cv2
import numpy as np

# Load the image
image = cv2.imread(r"E:\cv lab\spiderman.jpg")
cv2.imshow("original image",image)

# Rotate the Spider-Man object by 90 degrees clockwise
rows, cols = image.shape[:2]
center = (cols // 2, rows // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, -90, 1)  # Negative angle for clockwise rotation
rotated_spiderman = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Invert the colors of the rotated Spider-Man object
inverted_spiderman = cv2.bitwise_not(rotated_spiderman)

# Create a mask of the inverted Spider-Man object
mask = cv2.cvtColor(inverted_spiderman, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

# Combine the inverted Spider-Man object and the original background
result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask)) + \
         cv2.bitwise_and(inverted_spiderman, inverted_spiderman, mask=mask)

# Display the result
cv2.imshow('Inverted Spider-Man', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
