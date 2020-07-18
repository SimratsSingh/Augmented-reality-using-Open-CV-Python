import cv2
import numpy as np

frameW = 640
frameH = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameH)
cap.set(4, frameW)
cap.set(10, 150)
def empty(a):
    pass

cv2.namedWindow("trackbars")

cv2.resizeWindow("trackbars", 480,240)
cv2.createTrackbar("Hue min","trackbars",0,179,empty)
cv2.createTrackbar("Hue max","trackbars",179,179,empty)
cv2.createTrackbar("sat min","trackbars",0,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",0,255,empty)
cv2.createTrackbar("val max","trackbars",79,255,empty)

while True:
    success, img = cap.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min= cv2.getTrackbarPos("Hue min","trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "trackbars")
    s_min = cv2.getTrackbarPos("sat min", "trackbars")
    s_max = cv2.getTrackbarPos("sat max", "trackbars")
    v_min = cv2.getTrackbarPos("val min", "trackbars")
    v_max = cv2.getTrackbarPos("val max", "trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower= np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    mask =cv2.inRange(imgHSV,lower,upper)
    imgR = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("original", img)
    cv2.imshow("hsv", imgHSV)
    cv2.imshow("mask", imgR)
    cv2.waitKey(1)
