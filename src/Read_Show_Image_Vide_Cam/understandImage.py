import cv2
import numpy as np
# image = cv2.imread("../../Images/face.png")

# cv2 image is a numpy array
# print(image.dtype)
# print(image.ndim)
# cv2.imshow("Original", image)
# # convert image to grayscale
# # OpenCV read the image in BGR format contrast to RGB format of Pillow or other image processing tools.
# grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(grayImg.dtype)
# print(grayImg.ndim)
# print(grayImg)
# cv2.imshow("Grayscale", grayImg)

# resize the image

# arr = np.array(image)

# print(arr)
# print(arr.dtype)

kernel = np.ones((5, 5), np.uint8)
print(kernel)
cv2.waitKey(0)
