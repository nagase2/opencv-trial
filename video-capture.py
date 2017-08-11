import numpy as np
import cv2
'''
ビデオファイルを読み込み、グレイで表示するサンプル
'''
cap = cv2.VideoCapture('images/test.MOV')



while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # TODO: I wanted to drow a line onto the movie, but couldn't make it so far.
    #cv2.line(cap, (0, 0), (150, 150), (255, 255, 255), 15)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
