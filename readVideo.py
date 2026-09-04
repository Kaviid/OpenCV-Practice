import cv2 as cv

#--Reading Video in OpenCV ----------------------------------------------
capture = cv.VideoCapture("videos/kitten.mp4")

#For webcam
#capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()