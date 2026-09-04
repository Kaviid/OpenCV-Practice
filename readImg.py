import cv2 as cv

#Read img from photos fold and store that in img var
img = cv.imread("photos/cat.jpg")

#Pass 2 para - Window name and img
cv.imshow("Cat", img)

#It wait for infinite time of time cause time = 0
cv.waitKey(0)


