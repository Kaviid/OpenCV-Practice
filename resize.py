import cv2 as cv

#Resize and Rescale

def rescaleFrame(frame, scale=0.75): #This work with Images, Videos or Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimmension = (width,height)

    return cv.resize(frame, dimmension, interpolation=cv.INTER_AREA)


#Image resize
img = cv.imread("photos/cat.jpg") 
resized_img = rescaleFrame(img, 0.5)
cv.imshow("Cat", img) #Original Image
cv.imshow("Cat resized", resized_img) #Resized Image

cv.waitKey(0)