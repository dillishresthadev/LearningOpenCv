import cv2

video = cv2.VideoCapture("../Videos/bikes.mp4")

while True:
    success, frame = video.read()
    if success:
        cv2.imshow("output", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
