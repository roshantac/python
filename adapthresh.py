import cv2
import numpy as np
from matplotlib import pyplot as plt
cap=cv2.VideoCapture(0)
while(True):
	ret,img =cap.read()
	cv2.imshow('fam',img)
	img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img =cv2.medianBlur(img,5)
	ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	cv2.imshow('frame1',th2)
	cv2.imshow('fram2',th3)
	m=cv2.waitKey(1)
	if m &0xff==ord('s'):
		break
cv2.destroyAllWindows()
	
