from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread("lion.jpg")
cv.imshow("Lion",img)



# Translation
def translate(img, x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down

translated = translate(img,200,-200)
cv.imshow("Translated",translated)

# Rotating
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)
rotated_rotated = rotate(rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
rotated_rotated = rotate(rotated_rotated,45)
cv.imshow("Rotated_Rotated",rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Flipping
flip = cv.flip(img,0)
cv.imshow("Flip",flip)


cv.waitKey()
