
import numpy as np
import cv2
import matplotlib.pyplot as plt



cap = cv2.VideoCapture('images/people-walking.mp4')
#cap = cv2.VideoCapture('F:/20101005_宏子バックアップ/京音＆絵麻の動画/DSCF9593.AVI')

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    k= cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
