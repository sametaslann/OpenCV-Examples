import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

#1. Point the image a certain colour
blank[200:300,300:400] = 0,0,255

#2. Draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2 ),(0,255,0),thickness=-1)

#3. Draw a Circle 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),80,(255,0,0),thickness=2)

#4. Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(240,250,154),2)

#5. Write text
cv.putText(blank,"Go little rockstar",(0,100),cv.FONT_HERSHEY_TRIPLEX, 1.6, (255,255,255),)
cv.imshow("Text",blank)

cv.waitKey()