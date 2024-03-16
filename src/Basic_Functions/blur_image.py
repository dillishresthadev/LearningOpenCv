import cv2

img = cv2.imread("../../Images/car.jpg")

# We are doing the gaussian blur here. Ksize (Kernel size) is the sequence of odd number of size 2.
blurImg = cv2.GaussianBlur(img, (7, 7), 0)
# To increase the blur you can increase the kernel
cv2.imshow("Original", img)
cv2.imshow("Blur", blurImg)

# there are other blur methods
blurImg2 = cv2.blur(img, (7, 7))
cv2.imshow("Blur2", blurImg2)

# for Motion blur
# https://www.geeksforgeeks.org/opencv-motion-blur-in-python/
cv2.waitKey(0)
