import cv2
import numpy as np

cap = cv2.VideoCapture('images/test.MOV')

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    #drow lines into movie
    cv2.line(frame, (0, 0), (150, 150), (111, 255, 255), 15)
    cv2.line(mask, (0, 0), (150, 400), (255, 111, 255), 15)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()