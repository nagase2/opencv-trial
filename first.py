import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Garage = "Ferrari", "Honda", "Porsche", "Toyota"

for each_car in Garage:
    print(each_car)
'''
a = 10

img = cv2.imread('images/Dollar-128.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

cv2.imwrite('images/watchgray2.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

