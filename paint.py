import cv2
import numpy as np

frameW = 640
frameH = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameH)
cap.set(4, frameW)
cap.set(10, 150)
#enter the value from "setting my color" to the mycolor array. Right now thw color feeded is pink.
myColors = [130, 21, 171, 179, 255, 255]
myColorValues = [[255,0,255]]
#enter the BRG value of the color you want your object to draw on the screen

mypoints = []

def findColor(img, myColors):
    c=0
    newpoints=[]
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0:3])
    upper = np.array(myColors[3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    x,y = getContours(mask)
    cv2.circle(imageResult, (x,y),5,myColorValues[c],cv2.FILLED)
    if x!=0 and y!=0:
        newpoints.append([x,y,c])
        c+=1
    return newpoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(mypoints, myColorValues):
    for point in mypoints:
        cv2.circle(imageResult,(point[0],point[1]),5,myColorValues[0],cv2.FILLED)



while True:
    success, img = cap.read()
    imageResult = img.copy()
    newpoints = findColor(img, myColors)
    if len(newpoints)!=0:
        for newP in newpoints:
            mypoints.append(newP)
    if len(mypoints)!=0:
        drawOnCanvas(mypoints,myColorValues)
    cv2.imshow("result", imageResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

