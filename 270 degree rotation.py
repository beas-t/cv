import cv2
path=("C:/Users/hi/OneDrive/Pictures/cat.jpeg")
src=cv2.imread(path)
window_name='image'
image=cv2.rotate(src,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name,image)
cv2.waitKey(0)
