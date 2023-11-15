import cv2
import numpy as np
cap=cv2.VideoCapture("C:/Users/hi/Videos/Captures/Media Player 2023-11-02 13-31-23.mp4")
if(cap.isOpened()==False):
    print("Error opening video file")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret ==True:
        cv2.imshow('Frame',frame)
        if cv2.waitKey(250)&OxFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
            
        
