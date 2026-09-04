import cv2 as cv

#1. Change RGB color into Gray color
img = cv.imread("photos/cat.jpg")
cv.imshow("Original color",img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Gray color", gray)

#2. Image Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blured Image", blur)

#3. Create Edge Cascade
cany = cv.Canny(img, 175, 50)
cv.imshow("Canny Edges", cany)

cv.waitKey(0)