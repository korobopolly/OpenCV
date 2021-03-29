import sys
import time
import numpy as np
import cv2


img = cv2.imread('ch02\\hongkong.jpg')

tm = cv2.TickMeter()

tm.reset()

tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop()

print('time:', (time.time() - t1) * 1000) #파이썬 방식
print('Elapsed time: {}ms.'.format(tm.getTimeMilli())) #Open CV 방식
cv2.imshow('image',edge)
cv2.waitKey()

cv2.destroyAllWindows()

