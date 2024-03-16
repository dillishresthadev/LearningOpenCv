import cv2
img = cv2.imread("../../Images/documentscanner2.jpg")
# setting the threshold
t_lower = 100
t_higher = 120
# Increasing the value of Lower and upper threshold value, no of edges will decrease.
# Applying Canny Edge Detector
edge = cv2.Canny(img, t_lower, t_higher)

cv2.imshow("Original", img)
cv2.imshow("Edge", edge)

cv2.waitKey(0)
# for more information
# https://www.geeksforgeeks.org/real-time-edge-detection-using-opencv-python/
