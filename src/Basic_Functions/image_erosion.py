import cv2
import numpy as np
img = cv2.imread("../../Images/documentscanner2.jpg")
# setting the threshold
t_lower = 100
t_higher = 120
# Increasing the value of Lower and upper threshold value, no of edges will decrease.
# Applying Canny Edge Detector
edge = cv2.Canny(img, t_lower, t_higher)
# To increase the thickness of edge , we can use image dilation
kernel = np.ones((5, 5), np.uint8)
# Iteration value define how much thickness value we need
dilationImg = cv2.dilate(edge,kernel,iterations=1)
erosionImg = cv2.erode(dilationImg, kernel, iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Edge", edge)
cv2.imshow("Dilation", dilationImg)
cv2.imshow("Erosion", erosionImg)
cv2.waitKey(0)

# Dilation Increases the thickness of the edge
# Erosion decreases the thickness of the edge
