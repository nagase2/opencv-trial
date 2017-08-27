import cv2
import numpy as np

img = cv2.imread('images/watch.jpg',cv2.IMREAD_ANYCOLOR)

#ps = img[155,55]
#img[155,55] = [255,255,255]

px = img[55,55]
print("px1=",px)

px = img[100:150,11:150]
print("px2=",px)

# write a white box into the picture
# 左辺が四角の座標、右辺が塗りつぶす色を示す。
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)

# ここでwatch faceのイメージを取得し、左上に表示している。取得した画像と、表示領域のサイズは必ず一致している必要がある。
watch_face = img[37:112,87:214]
img[0:75,0:127] = watch_face


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()