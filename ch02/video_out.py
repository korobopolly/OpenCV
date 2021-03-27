import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #정수형 변환
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 60 #cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h)) #컬러영상 저장 객체

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame #프레임 반전
    edge=cv2.Canny(frame,50,150)
    edge_color=cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)
    out.write(edge_color)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('edge_color', edge_color)
    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
