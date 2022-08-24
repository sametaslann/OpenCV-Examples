import cv2 as cv
from cv2 import imread
import numpy as np

#Contour -> Hatlarını belirlemek 

img = imread("lion.jpg")
cv.imshow("lion",img)


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank",blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny",canny)

# ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
# cv.imshow("Thresh",thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours drawn", blank)

cv.waitKey(0)