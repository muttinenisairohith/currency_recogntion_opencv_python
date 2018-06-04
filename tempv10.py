import cv2
import numpy as np
import urllib
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.0.7:8080/shot.jpg'

while True:

    	# Use urllib to get the image and convert into a cv2 usable format
 	#imgResp=urllib.urlopen(url)
   	#imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
   	#img=cv2.imdecode(imgNp,-1)
	img=cv2.imread("10web2.jpg")
   	 # put the image on screen
   	cv2.imshow('IPWebcam',img)

    	#To give the processor some less stress
   	 #time.sleep(0.1) 


	# Convert it to grayscale
    	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#cv2.imshow("img1",img_gray)
	# Read the template
	template = cv2.imread('10gg',0)
	template1 = cv2.imread('10gg1.jpeg',0)
	template2=cv2.imread('10gg2.jpeg',0)
	template3= cv2.imread('10gg3.jpeg',0)
	template4 = cv2.imread('10gg4.jpg',0)
	template5 = cv2.imread('10gg5.jpg',0)
	template6=cv2.imread('10gg6.jpg',0)
	template7= cv2.imread('10gg7.jpg',0)
	template8=cv2.imread('10gg8.jpg',0)
	template9= cv2.imread('10gg9.jpg',0)
	#cv2.imshow("img2",template)
	# Store width and heigth of template in w and h
	w, h = template.shape[::-1]
	w1, h1 = template1.shape[::-1]
	w2, h2 = template2.shape[::-1]
	w3, h3 = template3.shape[::-1] 
	w4, h4 = template4.shape[::-1]
	w5, h5 = template5.shape[::-1]
	w6, h6 = template6.shape[::-1]
	w7, h7 = template7.shape[::-1] 
	w8, h8 = template8.shape[::-1]
	w9, h9 = template9.shape[::-1] 
	# Perform match operations.
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	res1 = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
	res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
	res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED) 
	res4 = cv2.matchTemplate(img_gray,template4,cv2.TM_CCOEFF_NORMED)
	res5 = cv2.matchTemplate(img_gray,template5,cv2.TM_CCOEFF_NORMED)
	#res6 = cv2.matchTemplate(img_gray,template6,cv2.TM_CCOEFF_NORMED)
	res7 = cv2.matchTemplate(img_gray,template7,cv2.TM_CCOEFF_NORMED) 
#	res8 = cv2.matchTemplate(img_gray,template8,cv2.TM_CCOEFF_NORMED)
	res9 = cv2.matchTemplate(img_gray,template9,cv2.TM_CCOEFF_NORMED)
	# Specify a threshold
	threshold = 0.7

	# Store the coordinates of matched area in a numpy array
	loc = np.where( res >= threshold) 
	loc1 = np.where( res1 >= threshold) 
	loc2 = np.where( res2 >= threshold) 
	loc3 = np.where( res3 >= threshold) 
	loc4 = np.where( res4 >= threshold) 
	loc5 = np.where( res5 >= threshold) 
#	loc6 = np.where( res6 >= threshold) 
	loc7 = np.where( res7 >= threshold) 
#	loc8 = np.where( res8 >= threshold) 
	loc9 = np.where( res9 >= threshold) 

	# Draw a rectangle around the matched region.
	for pt in zip(*loc[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
	for pt in zip(*loc1[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w1, pt[1] + h1), (255,255,255), 2)
	for pt in zip(*loc2[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w2, pt[1] + h2), (255,0,255), 2)
	for pt in zip(*loc3[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w3, pt[1] + h3), (0,0,255), 2)
	for pt in zip(*loc4[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w4, pt[1] + h4), (0,255,255), 2)
	for pt in zip(*loc5[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w5, pt[1] + h5), (255,255,255), 2)
#	for pt in zip(*loc6[::-1]):
#	    cv2.rectangle(img, pt, (pt[0] + w6, pt[1] + h6), (255,0,255), 2)
	for pt in zip(*loc7[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w7, pt[1] + h7), (0,0,255), 2)
#	for pt in zip(*loc8[::-1]):
#	    cv2.rectangle(img, pt, (pt[0] + w8, pt[1] + h8), (255,0,255), 2)
	for pt in zip(*loc9[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w9, pt[1] + h9), (0,0,255), 2)



	# Show the final image with the matched area.
	cv2.imshow('Detected',img)
	cv2.waitKey(1)
