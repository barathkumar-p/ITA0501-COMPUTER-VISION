import cv2 as cv
import numpy as np

# Load the image
image = cv.imread(r"E:\cv lab\bike.jpg", cv.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
img_gauss = cv.GaussianBlur(image, (3, 3), 0)

# Define Prewitt kernels
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Calculate Prewitt gradients
img_prewittx = cv.filter2D(img_gauss, cv.CV_64F, kernel_x)
img_prewitty = cv.filter2D(img_gauss, cv.CV_64F, kernel_y)

# Calculate the gradient magnitude
img_prewitt = cv.magnitude(img_prewittx, img_prewitty)

# Normalize the gradient magnitude to the range [0, 255]
img_prewitt = cv.normalize(img_prewitt, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

# Display the original and Prewitt edge detection results
cv.imshow("Original Image", image)
cv.imshow("Prewitt Edge Detection", img_prewitt)

# Wait for a key press and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()
