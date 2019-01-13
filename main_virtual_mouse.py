import cv2
import numpy as np
from pynput.mouse import Button, Controller
import pyautogui

SX,SY=pyautogui.size() #Gets the size of screen 
MX,MY =(SX/5)+30, (SY/5)+30 
WW,WH=450,450      				# Width, Height of Live Camera
FX,FY=(WW-MX)/2,(WH-MY)/2		# FRAMES TopLeft Coordinate
LB_G=np.array([80,80,40])   	# GREEN HSV LowerBound
UB_G=np.array([100,255,255])	# GREEN HSV UpperBound
SE=np.ones((5,5))           	#will be used for dilation and erosion 
capture=cv2.VideoCapture(0) 	# 0 - Capture by Using First Camera

mouse=Controller()
while capture.isOpened():		 # A Controller for sending Virtual Mouse Events to the System.
	var,frame=capture.read()	 # Captures Video Frame by Frame
	cv2.resize(frame,(MY,MX))
	ROI=frame[FY:FY+MY+90,FX:FX+MX]#	Region of Interest, [C1:C1+N, R1+R1+M] LeftColumnPixel LeftRowPixel
	frame_hsv=cv2.cvtColor(ROI,cv2.COLOR_BGR2HSV) # Converts BGR Color_Space Frame into HSV color_space
	mask=cv2.inRange(frame_hsv,LB_G,UB_G)	# Create A Binary Image, Pixel with InRange == 1
	mask_o=cv2.morphologyEx(mask,cv2.MORPH_OPEN,SE)# Erosion followed by Dilation
	mask_c=cv2.morphologyEx(mask_o,cv2.MORPH_CLOSE,SE)# Dilation followed by Erosion
	cv2.rectangle(frame,(FX,FY),(FX+MX,FY+MY),(255,0,0),3)# SWIPE
	cv2.rectangle(frame,(FX,FY+MY),((FX+MX)/2-30,FY+MY+90),(255,0,255),3) # LEFT
	cv2.rectangle(frame,((FX+MX)/2-30,FY+MY),(FX+MX,FY+MY+90),(255,0,255),3)# RIGHT
	#	Draws Rectangle TopLeft BottomRight RGB Thickness
	_,outline,heir=cv2.findContours(mask_c,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	Object=[]
	leftb=[]
	rightb=[]
	for x in outline:
		if cv2.contourArea(x)>150:
			LX,LY,W,H = cv2.boundingRect(x)
			if (LY<FY+MY) and len(Object)<3:
				Object.append(x)
			if (LX<(FY+MX)/2-30 and LY>FY+MY) and len(leftb)==0 :
				leftb.append(x)
			if (LX>(FY+MX)/2-30 and LY>FY+MY) and len(rightb)==0:
				rightb.append(x)
	if len(Object)==1:
		LX,LY,W,H =cv2.boundingRect(Object[0])
		cv2.drawContours(ROI,Object,-1,(255,0,0),3)
		cv2.rectangle(ROI,(LX,LY),(LX+W,LY+H),(0,255,0),2)
		# 	cv2.rectangle(image, TL, RB, color, thickness) 
		cv2.circle(ROI,(LX,LY),5,(0,0,255),-1)
		#	cv2.circle(image, center, radius, color, thickness)
		mouse.release(Button.left)
		mouse.position=(LX*5,LY*5)
	if len(Object)==2 : # SINGLE CLICK

		LX1,LY1,W1,H1 =cv2.boundingRect(Object[0])
		LX2,LY2,W2,H2 =cv2.boundingRect(Object[1])
		cv2.drawContours(ROI,Object,-1,(255,0,0),3)
		cv2.rectangle(ROI,(LX1,LY1),(LX1+W1,LY1+H1),(0,255,0),2)
		cv2.rectangle(ROI,(LX2,LY2),(LX2+W2,LY2+H2),(0,255,0),2)
		mouse.press(Button.left)
		mouse.release(Button.left)
	if len(leftb)!=0:	# DOUBLE CLICK
		LX,LY,W,H=av2.boundingRect(leftb[0])
		cv2.drawContours(ROI,leftb[0],-1,(255,0,0),3)
		cv2.rectangle(ROI,(LX,LY),(LX+W,LY+H),(0,255,0),2)
		mouse.release(Button.left)
		mouse.click(Button.left,2)
	if len(rightb)!=0:
		LX,LY,W,H = av2.boundingRect(rightb[0])
		cv2.drawContours(ROI,rightb[0],-1,(255,0,0),3)
		cv2.rectangle(ROI,(LX,LY),(LX+W,LY+H),(0,255,0),2)
		mouse.press(Button.right)
		mouse.release(Button.right)
	
	cv2.imshow("frame",frame)
	if cv2.waitKey(1) & 0xFF == 27:

		break
capture.release()
cv2.destroyAllWindows()

#colours
#	YELLOW : (20, 100, 100) (30, 255, 255)

#	RED : (0, 70, 50) (10, 255, 255)

#	BLUE : (110, 50, 50) (130, 255, 255)

#	GREEN : (33, 80, 40) (102, 255, 255)

#	SKIN : (0,20,70) (20,255,255)
