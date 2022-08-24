from random import gauss
import cv2 as cv

img = cv.imread("Istanbul.jpg")
cv.imshow("Istanbul",img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow("Average", average) 

# Gaussion Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian",gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow("Median", median)

# Bilateral 
bilateral = cv.bilateralFilter(img, 10 , 35, 25)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)
