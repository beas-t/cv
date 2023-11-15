import cv2
import numpy as np
image=cv2.imread("C:/Users/hi/OneDrive/Pictures/cat.jpeg")
tx=50
ty=30
M=np.float32([[1,0,tx],
              [0,1,ty]])
result=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow('Transformed image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
