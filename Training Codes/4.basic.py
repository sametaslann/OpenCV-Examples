from types import CoroutineType
import cv2 as cv

img = cv.imread("lion.jpg")
cv.imshow("Lion",img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#Blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#Edge Cascade (eşik değerleri (200,200))
canny = cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

#Dilating the Image (genişletme)
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

#Eroding (Aşındırma)
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

#Resize
resized = cv.resize(img, (500,800)) #interpolation= cv.INTER_LINEAR)
cv.imshow("Resized",resized)

#Cropping
cropped = img[300:400, 400:600]
cv.imshow("Cropped",cropped)

cv.waitKey(0)