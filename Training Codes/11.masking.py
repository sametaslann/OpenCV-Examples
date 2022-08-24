import cv2 as cv
from cv2 import circle
from cv2 import bitwise_and
from cv2 import rectangle
import numpy as np

img = cv.imread("Istanbul.jpg")
cv.imshow("Istanbl",img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Image", blank)


# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 ), 100, 255, -1)
# cv.imshow("Mask", mask)


circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 ), 200, 255, -1)
cv.imshow("circle" , circle)

rectangle = cv.rectangle(blank.copy(),(250,105), (570, 425), 255, -1 )
cv.imshow("rectangle" , rectangle)

weird_shape = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise and" ,weird_shape)

masked = cv.bitwise_and(img,img, mask = weird_shape)
cv.imshow("Masked Image", masked)

cv.waitKey(0)