import cv2
import numpy as np
 
# Read the main image
img_rgb = cv2.imread('10web2.jpg')
cv2.imshow('img',img_rgb)
 
# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#cv2.imshow("img1",img_gray)
# Read the template
template = cv2.imread('10gg',0)
template1 = cv2.imread('10gg1.jpeg',0)
template2=cv2.imread('10gg2.jpeg',0)
template3= cv2.imread('10gg3.jpeg',0)
#cv2.imshow("img2",template)
# Store width and heigth of template in w and h
w, h = template.shape[::-1]
w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1] 
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
res1 = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED) 
# Specify a threshold
threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold) 
loc1 = np.where( res1 >= threshold) 
loc2 = np.where( res2 >= threshold) 
loc3 = np.where( res3 >= threshold) 

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
for pt in zip(*loc1[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (255,255,255), 2)
for pt in zip(*loc2[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (255,0,255), 2)
for pt in zip(*loc3[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0,0,255), 2)

# Show the final image with the matched area.
cv2.imshow('Detected',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
