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

#4. Dilatting image
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

#  📝 Dilation — Simple Notes

#   cv.dilate() → makes the white/edge regions thicker.
#   Kernel (7,7) → uses a 7×7 area to expand the pixels.
#   iterations=3 → dilation is repeated 3 times, so the effect is stronger.
#   It is mainly used to connect broken edges and make edges more visible.
#   It can help before finding contours/shapes.

#   Easy idea
#   Canny → thin edges → Dilation → thicker/connected edges🔗
#   Remember: Bigger kernel or more iterations = more dilation.


cv.waitKey(0)