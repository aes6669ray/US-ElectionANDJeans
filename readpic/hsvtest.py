import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread("41094.jpg")
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# cv2.imshow("img",img)



cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640,320)

cv2.createTrackbar("Hue min","trackbar",0,179,empty)
cv2.createTrackbar("Hue max","trackbar",179,179,empty)
cv2.createTrackbar("Sat min","trackbar",0,255,empty)
cv2.createTrackbar("Sat max","trackbar",255,255,empty)
cv2.createTrackbar("Val min","trackbar",0,255,empty)
cv2.createTrackbar("Val max","trackbar",255,255,empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    Hue_min = cv2.getTrackbarPos("Hue min","trackbar")
    Hue_max = cv2.getTrackbarPos("Hue max","trackbar")
    Sat_min = cv2.getTrackbarPos("Sat min","trackbar")
    Sat_max = cv2.getTrackbarPos("Sat max","trackbar")
    Val_min = cv2.getTrackbarPos("Val min","trackbar")
    Val_max = cv2.getTrackbarPos("Val max","trackbar")
    print(Hue_min,Hue_max,Sat_min,Sat_max,Val_min,Val_max)

    lower = np.array([Hue_min,Sat_min,Val_min])
    upper = np.array([Hue_max,Sat_max,Val_max])

    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("img",img)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    if cv2.waitKey(1) == ord("q"):
        break