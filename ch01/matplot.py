import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('ch01\cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # RGB순서로 변환

plt.axis('off') #눈금표 지우기
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('ch01\cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB) #1행 2열로 나누고 1번째 자리에 출력
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray') #1행 2열로 나누고 2번째 자리에 출력
plt.show()
