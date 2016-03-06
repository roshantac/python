import cv2
import numpy

cap=cv2.VideoCapture(0)
while (True) :
	ret,frame=cap.read()
	cv2.imshow('video',frame)
	if cv2.waitKey(1) & 0x0ff==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
