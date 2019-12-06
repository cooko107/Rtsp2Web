import cv2

cap = cv2.VideoCapture('rtsp://88888888:xiolift123@10.19.31.25/h265/ch1/main/av_stream')

while True:
    ret , frame= cap.read()
    print(frame.shape)