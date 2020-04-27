#Harsh Mittal     harshmittal2209@gmail.com
import numpy as np
import cv2
import matplotlib.pyplot as plt

#%matplotlib inline

drawing = False
ex=-1
ey=-1

def DrawRectangle(event, x, y, flags, params):
	global ex, ey, drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ex,ey = x,y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.rectangle(img,(ex,ey),(x,y),(100,100,100),-1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.rectangle(img,(ex,ey),(x,y),(100,100,100),-1)


cv2.namedWindow('mw')
cv2.setMouseCallback('mw',DrawRectangle)

img = np.zeros((1000,1000,3),np.int8)

while True:
	cv2.imshow('mw',img)
	if cv2.waitKey(5) & 0xFF == 27:
		break
cv.destroyALLWindows()


