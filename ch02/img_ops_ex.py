import numpy as np
import cv2

#영상 생성하기
'''
img1=np.empty((240,320),dtype=np.uint8) #흑백영상 값:쓰레기
img2=np.zeros((240,320,3),dtype=np.uint8) #컬러영상 값:0
img3=np.ones((240,320,3),dtype=np.uint8)*255 #컬러영상 값:255
img4=np.full((240,320),128,dtype=np.uint8) #흑백영상 값:128
'''

img1=cv2.imread('ch02\HappyFish.jpg')
img2=img1[40:120,30:150]
img3=img1[40:120,30:150].copy()

#img2.fill(0)
cv2.circle(img2,(50,50),20,(0,0,255),2) #좌표,반지름,색상,두께

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
#cv2.imshow('img4',img4)

cv2.waitKey()