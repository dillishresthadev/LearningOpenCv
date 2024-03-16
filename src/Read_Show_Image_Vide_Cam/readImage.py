import cv2

# Reading the image
image = cv2.imread("../../Images/car.jpg")

# Showing the image in dialog
cv2.imshow("Original Image", image)

# Waiting till window is closed.
# waitKey take millisecond parameter. 1 = 1 millisecond , 0 is for infinity
cv2.waitKey(0)
