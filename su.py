import cv2
import numpy
img1=cv2.imread('lena.jpg')
cv2.imshow('image',img1)
k=cv2.waitKey(1) & 0xFF
	if (k==ord('s')):
		cv2.destroyAllWindows()
