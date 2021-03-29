import numpy as np
import cv2

def on_level_changed(pos):
    global img

    level=pos*16
    if level>=255:
        level=255
    '''
    level=np.clip(level,0,255)
    '''

    img[:,:]=level
    cv2.imshow('image',img)

img = np.zeros((480, 640), np.uint8) #grayscale 영상 0~255



cv2.namedWindow('image')
cv2.imshow('image', img) #창 생성 후에 사용
cv2.createTrackbar('level','image',0,16,on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()