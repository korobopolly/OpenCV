import sys
import cv2


print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('ch01\cat.bmp',cv2.IMREAD_GRAYSCALE) #흑백 이미지 처리

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('ch01\cat_gray.jpg',img)

cv2.namedWindow('image') #cv2.WINDOW_NORMAL 영상 크기를 창 크기에 맞게
                         #cv2.WINDOW_AUTOSIZE 창 크기를 영상 크기에 맞게 (기본값)
cv2.imshow('image',img)

while True:
    if cv2.waitKey()==27: #ord('a'):
        break

cv2.destroyWindow('image')