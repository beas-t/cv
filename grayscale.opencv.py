import cv2
path="C:/Users/hi/OneDrive/Pictures/cat.jpeg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
