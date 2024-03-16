import cv2

img = cv2.imread("../../Images/car.jpg")

# here need to understand the format of color in opencv is BGR instead of RGB
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",img)
cv2.imshow("Gray", grayImg)

cv2.waitKey(0)
