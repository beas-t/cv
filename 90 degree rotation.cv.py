import cv2
path=("C:/Users/hi/OneDrive/Pictures/cat.jpeg")
src=cv2.imread(path)
image=cv2.rotate(src,cv2.ROTATE_180)
cv2.imshow("Image",image)
cv2.waitKey(0)
