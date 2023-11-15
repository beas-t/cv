import cv2
import numpy as np

def perspective_transform(frame):
    height, width, _ = frame.shape
    src_points = np.float32([[0, height], [width, height], [0, 0], [width, 0]])
    dst_points = np.float32([[0, height], [width, height], [width*0.2, 0], [width*0.8, 0]])
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    transformed_frame = cv2.warpPerspective(frame, matrix, (width, height))

    return transformed_frame

video_capture = cv2.VideoCapture('input_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video.avi'), fourcc, 30, (int(video_capture.get(3)), int(video_capture.get(4)))

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break

    transformed_frame = perspective_transform(frame)

    output_video.write(transformed_frame)

    cv2.imshow('Perspective Transformed Video', transformed_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video_capture.release()
output_video.release()
cv2.destroyAllWindows()
