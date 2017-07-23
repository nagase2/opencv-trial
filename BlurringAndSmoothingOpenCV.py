import cv2
import numpy as np

cap=cv2.VideoCapture('images/test.MOV')

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    #フィルタータイプ１
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    cv2.imshow('Averaging',smoothed)

    #フィルタータイプ２
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    cv2.imshow('Gaussian Blurring', blur)

    #フィルター３
    median = cv2.medianBlur(res, 15)
    cv2.imshow('Median Blur', median)

    #フィルター４
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('bilateral Blur', bilateral)

    #そのまま表示
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
