from asyncore import write
import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture(1,cv.CAP_DSHOW)
radius = 0

while True:
    ret,frame = cap.read()
    if frame is None:
        break
    original = frame.copy()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([160,100,20])
    upper_red = np.array([179,255,255])

    red_mask = cv.inRange(hsv,lower_red,upper_red)
    red_color = cv.bitwise_and(frame, frame, mask= red_mask)

    gray = cv.cvtColor(red_color, cv.COLOR_BGR2GRAY)
    gray_blurred = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    circles = cv.HoughCircles(gray_blurred, cv.HOUGH_GRADIENT, 1,200,param1=50,
                              param2=30,minRadius=0,maxRadius=100)


    height, width, channels = frame.shape
    upper_left = (width // 3, height // 3)
    bottom_right = (width * 3 // 3, height * 3 // 3)
    # draw in the image
    cv.rectangle(original, (315-radius,225-radius), (325+radius,235+radius), (0, 0, 255), thickness=1)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x,y,r) in circles:
            radius = r
            if x<330+radius and x>310-radius and y>220-radius and y<240+radius:
                print(circles)
                print("Founded..")
                cv.circle(original, (x,y) ,r , (255,255,0),2)
                cv.circle(original, (x,y) ,1 , (255,255,0),3)

    cv.imshow("Circle", original)        
    #cv.imshow("Red", red_color)  

    k = cv.waitKey(5) & 0xFF 

    if k == ord('q'):
        break

    