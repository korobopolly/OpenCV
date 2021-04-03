import sys
import numpy as np
import cv2

# 그레이스케일 영상 불러오기
src = cv2.imread('ch03\\lenna.bmp')

dst=cv2.add(src,(100,100,100,0)) #스칼라 - 4개의 실수 값으로 구성된 튜플, B G R A
#dst=np.clip(src+100.,0,255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()