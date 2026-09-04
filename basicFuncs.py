import cv2 as cv

#1. Change RGB color into Gray color
img = cv.imread("photos/cat.jpg")
cv.imshow("Original color",img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Gray color", gray)

cv.waitKey(0)