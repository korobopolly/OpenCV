import sys
import cv2

#마스크 영상을 이용한 영상 합성
src=cv2.imread('ch02\\opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
mask=src[:,:,-1]
src=src[:,:,0:3]
dst=cv2.imread('ch02\\field.bmp',cv2.IMREAD_COLOR)

h,w=src.shape[:2]

crop=dst[30:h+30,30:w+30]

cv2.copyTo(src,mask,crop)
#dst[mask>0]=src[mask>0]

cv2.imshow('src',src)
cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.waitKey()
