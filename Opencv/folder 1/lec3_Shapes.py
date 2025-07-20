import cv2 as cv
import numpy as np

# draw and write on images

# Creation of a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")
cv.waitKey(0)

# Paint image a certain color :
blank[:] = 0, 0, 255
cv.imshow('Image', blank)
cv.waitKey(0)

# Coloring a certain portion
# blank[200:300 , 300:400] = 0, 255, 0
# cv.imshow('Image', blank)
# cv.waitKey(0)

# Drawing rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Image', blank)
cv.waitKey(0)

# filling a certain color :
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow('Image', blank)
cv.waitKey(0)

# Circle
cv.circle(blank, (250,250), blank.shape[1]//2, blank.shape[0]//2) # image bytecode, centre