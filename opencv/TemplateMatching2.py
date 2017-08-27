import cv2
import numpy as np

img_rgb = cv2.imread('matchingImages/desktop.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('matchingImages/pyicon.png',0)
w, h = template1.shape[::-1]

res = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where (res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    print("found it!")


template2 = cv2.imread('matchingImages/menu.png',0)
w, h = template2.shape[::-1]

res = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where (res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 111, 255), 2)
    print("found memu!")


cv2.imshow('Detected',img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()