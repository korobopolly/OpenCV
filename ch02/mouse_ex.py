import sys
import numpy as np
import cv2

oldx=oldy=-1

def on_mouse(event,x,y,flags,param):
    global img,oldx,oldy

    if event==cv2.EVENT_LBUTTONDOWN:
        oldx,oldy=x,y
        print('EVENT_LBUTTONDOWN: {}, {}'.format(x,y))
    elif event==cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: {}, {}'.format(x,y))
    elif event==cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON: #flags는 &연산과 사용하는 것이 좋다
            #print('EVENT_MOUSEMOVE: {}, {}'.format(x,y)) #마우스 좌표 출력
            #cv2.circle(img,(x,y),5,(0,0,255),-1) #끊김이 있음
            cv2.line(img,(oldx,oldy),(x,y),(0,0,255),5,cv2.LINE_AA)
            cv2.imshow('image',img) 
            oldx,oldy=x,y


img = np.ones((480,640,3), dtype=np.uint8)*255 #세로, 가로

cv2.namedWindow('image')
cv2.imshow('image',img) #창 호출 이후에 마우스콜백 함수 입력
cv2.setMouseCallback('image',on_mouse)

cv2.waitKey()

cv2.destroyAllWindows()