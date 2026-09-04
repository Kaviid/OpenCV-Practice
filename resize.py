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


#TODO : Make sure to comment Image resize code when running video resize code, unless it'm messy
#Video resize
capture = cv.VideoCapture("videos/kitten.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    frame_resized_05 = rescaleFrame(frame,scale=0.3)

    cv.imshow("Kitten Video", frame) #Orginal frame
    # cv.imshow("Resized Kitten Video scale = 0.75", frame_resized) #Resized frame scale 0.75
    cv.imshow("Resized Kitten Video scale = 0.5", frame_resized_05) #Resized frame scale 0.5

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)