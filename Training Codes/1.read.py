import cv2 as cv



capture = cv.VideoCapture("Testing PegSolitaire Solitaire 2022-01-27 18-25-53.mp4")
while True:
     isTrue, frame = capture.read()
     cv.imshow("Video",frame)
     if cv.waitKey(20) & 0xFF== ord('d'):
         break
capture.release()
cv.destroyAllWindows()


cv.waitKey(0)