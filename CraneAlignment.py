from asyncore import write
import math
import cv2 as cv
import numpy as np
import time
#RTSP
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
radius = 0

while True:
    ret,frame = cap.read()
    if frame is None:
        break
    originalFrame = frame.copy()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([160,100,20])
    upper_red = np.array([179,255,255])

    red_mask = cv.inRange(hsv,lower_red,upper_red)
    red_color = cv.bitwise_and(frame, frame, mask= red_mask)

    gray = cv.cvtColor(red_color, cv.COLOR_BGR2GRAY)
    gray_blurred = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    circles = cv.HoughCircles(gray_blurred, cv.HOUGH_GRADIENT, 1,200,param1=50,
                              param2=30,minRadius=0,maxRadius=100)

#param2-1 yuvarlak algılama  max min radius

    # draw in the image
    cv.rectangle(originalFrame, (315-radius,225-radius), (325+radius,235+radius), (0, 0, 255), thickness=1)

    if circles is not None:
        
        circles = np.round(circles[0, :]).astype("int")
        
        for (circ_x,circ_y,circ_r) in circles:
            radius = circ_r
            horizontalDist = 1500/circ_r
            verticalPx = math.sqrt(abs(320-circ_x)*abs(320-circ_x) + abs(230-circ_y)*abs(230-circ_y))
            print(radius)
            verticalDistance = (horizontalDist)/500 * (verticalPx )
            # print("Horizontal: " , horizontalDist)
            # print("vertical: " , verticalDistance)
            
            
            degree = (180/math.pi)*np.arctan(verticalDistance/horizontalDist)
            degree = round(degree,2)
            finalStr = str(degree) + "degree  Dist:" + str(round(horizontalDist,1)) 
            
            centerOfCamera = (320, 230)
            centerOfCircle = (circ_x, circ_y)
            blueColor = (255, 0, 0)
            CyanColor = (255,255,0)
            
            cv.line(img=originalFrame, pt1 = centerOfCamera, pt2=centerOfCircle, color=blueColor, thickness=3, lineType=5, shift=0)
            cv.putText(originalFrame, str(finalStr), (30,30), cv.FONT_HERSHEY_SIMPLEX, 1, blueColor, thickness=2)
            
            if circ_x < 330+radius and circ_x > 310-radius and circ_y > 220-radius and circ_y < 240+radius:
                print("Coordinates: " , circles)
                cv.circle(originalFrame, (circ_x,circ_y) ,circ_r , CyanColor,2)
                cv.circle(originalFrame, (circ_x,circ_y) ,1 , CyanColor,3)

    cv.imshow("Circle", originalFrame)        
    #cv.imshow("Red", red_color)  

    k = cv.waitKey(5) & 0xFF 

    if k == ord('q'):
        break

    
