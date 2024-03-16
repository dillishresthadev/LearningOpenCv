import cv2
import numpy as np

image = cv2.imread("../Images/car.jpg")

cv2.imshow("Original Image",image)

cv2.waitKey(0)