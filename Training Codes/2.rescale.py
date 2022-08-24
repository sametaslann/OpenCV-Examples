
import cv2 as cv

img = cv.imread("lion.jpg")

def rescaleFrame(frame,scale = 0.75):
    #images, Videos and Live Video
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live Video
    capture.set(3,width)
    capture.set(4,height)


resized_img = rescaleFrame(img)
cv.imshow("Image",img)
cv.imshow("Resized Image",resized_img)


#Reading Video
capture = cv.VideoCapture("peg.mp4")
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.2 )

    cv.imshow("Video",frame)
    cv.imshow("Video Resized",frame_resized)
    if cv.waitKey(20) & 0xFF== ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)