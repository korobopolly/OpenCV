import sys
import cv2

cap=cv2.VideoCapture(0) #cap=cv2.VideoCapture(0)
#cap.open('ch02\\video1.mp4')

if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(w,h)

#w=cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
#h=cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

while True:
    ret, frame=cap.read()

    if not ret:
        break

    edge=cv2.Canny(frame,50,150)

    cv2.imshow('frame',frame)
    cv2.imshow('edge',edge)
    if cv2.waitKey(20)==27:
        break

cap.release()
cv2.destroyAllWindows()