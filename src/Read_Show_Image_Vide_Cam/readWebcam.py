import cv2

# Reading the video from webcam
# use id of the web camp, using 0 for the laptop default webcam, if you have external webcam you need to put the id of
# that webcamp in cv2.VideoCapture
video = cv2.VideoCapture(0)
# video has many property which you can set by selecting its propertyId and setting the value.
# below is example of changing the width (propId:3) , height (propId:4), you can also change the brightness (propId:10)
# video.set(3, 200)
# video.set(4, 200)


while True:
    # read success status and frame of the video
    success, frame = video.read()
    if success:
        # if success show the image by image frame
        cv2.imshow("output", frame)
        # wait till the video end and close the window (break) or immediately close the window when 'q' char is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# releasing the video captured by video variable in above
video.release()
# destroying all window to release the memory
cv2.destroyAllWindows()
