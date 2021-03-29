import sys
import numpy as np
import cv2


img = cv2.imread('ch02\\cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    key=cv2.waitKey() #키 값을 한번만 기다림 (중요도 높음)
    if key==27:
        break
    elif key==ord('i')or key==ord('I'):
        img=~img
        cv2.imshow('~img',~img)

cv2.destroyAllWindows()
