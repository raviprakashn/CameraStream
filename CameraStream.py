# this script reads video from live camera by using IP or reads data from the video. if you want read from the video file give you image file locate to the input variable

import cv2
import numpy as np
import os

input = "udp://10.60.62.52:8080"
#input = "/home/rmeda/Videos/guns.mp4"
cap = cv2.VideoCapture(input)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
ret, frame = cap.read()
fheight, fwidth = frame.shape[:-1]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
i = 0
file_name = "capture"+str(i)+".avi"
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", int(fwidth/2), int(fheight/2))
while True:
	file_name = "capture"+str(i)+".avi"
	if not os.path.exists(file_name):
		break
	i += 1

out = cv2.VideoWriter(file_name, fourcc, 30.0, (fwidth,fheight))
while cap.isOpened():
	ret, frame = cap.read()
	#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
	#cv2.resizeWindow('image', 480,640)
	#cv2.rectangle(frame, (1017,35), (1040,935), (0, 0,255), 2)
	cv2.imshow("image", frame)
	cv2.waitKey(1)
	out.write(frame)

cap.release()
out.release()

