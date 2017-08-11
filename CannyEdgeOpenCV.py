import cv2
import numpy as np

#cap = cv2.VideoCapture('images/test.MOV');
cap=cv2.VideoCapture('images/test.MOV')

while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)






    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()