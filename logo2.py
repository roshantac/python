import cv2
import numpy
img1=cv2.imread('messi.jpeg')
img2=cv2.imread('lena2.jpg')
cv2.imshow('lgo1',img2)
#get row and column size
rows,colums,channel = img2.shape
roi=img1[0:rows,0:colums]

#creting mask logo

grayimg=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(grayimg,100,255,cv2.THRESH_BINARY)
maskinv=cv2.bitwise_not(mask)
cv2.imshow('frame1',mask)
cv2.waitKey(7000)
cv2.imshow('frame2',maskinv)
cv2.waitKey(6000)
#blacking out logo
img1_bg=roi

#taking logo region from image
img2_fg=img2
cv2.imshow('kl',img2_fg)

#put logo in ROI and modify the main image
dst=cv2.add(img1_bg,img2_fg)
cv2.imshow('step',dst)
img1[0:rows,0:colums]=dst
cv2.imshow('res',img1)
cv2.waitKey(0)

