import cv2

# Reading the video
video = cv2.VideoCapture("../../Videos/bikes.mp4")

while True:
    # read success status and frame of the video
    success, frame = video.read()
    if success:
        # if success show the image by image frame
        cv2.imshow("output", frame)
        # wait till the video end and close the window (break) or immediately close the window when 'q' char is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        # you will need to click on space to run the video . continue press 'space' will run the video.
        # As it is waiting till the infinity. cv2.waitkey(0) is never changing the frame.
        # if cv2.waitKey(0) & 0xFF == ord("q"):
        #    break
        # to decrease the speed of video, you will just increase the cv2.waitkey variable.
        # if 100 then frame will change per 100 millisecond
        # so to delay we just increase the value of cv2.waitkey
    else:
        break

# releasing the video captured by video variable in above
video.release()
# destroying all window to release the memory
cv2.destroyAllWindows()
