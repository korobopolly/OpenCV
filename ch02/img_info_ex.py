import sys
import cv2

img1=cv2.imread('ch02\cat.bmp',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('ch02\cat.bmp',cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Load Failed')
    sys.exit()

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

if img1.ndim==2:
    print('img1 is a grayscale')

if len(img1.shape)==2:
    print('img1 is a grayscale')

h,w=img1.shape[:2]
print('w x h = {} x {}'.format(w,h))

h,w=img2.shape[:2] #3개짜리 튜플값을 2개만 가져온다.
print('w x h = {} x {}'.format(w,h))

'''
for y in range(h):
    for x in range(w):
        img1[y,x]=0
        img2[y,x]=(0,0,255)
'''

img1[:,:]=0
img2[:,:]=(0,0,255)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey()
