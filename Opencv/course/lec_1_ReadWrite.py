# What is reading writing ?

# To extract an image or writing we use reading writing
    # read to interpret the images
    # save for analysis or preprocessing
    # matrix gets read and we can do modification or anything 
    # of use.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

# Read image
def readImage() :
    root = os.getcwd() # mains get current working directory
    imgPath = os.path.join(root, 'Opencv/image/kitty.jpg') # combines the base folder with getcwd item

    # work of opencv
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow('img', img)
    cv.waitKey(0)

# Write image
def writeImage():
    root = os.getcwd() # mains get current working directory
    imgPath = os.path.join(root, 'Opencv/image/kitty.jpg') # combines the base folder with getcwd item
    img = cv.imread(imgPath)
    outputPath = os.path.join(root, 'Opencv/image/output.jpg')
    cv.imwrite(outputPath, img)



if __name__ == '__main__' :
    readImage()
    writeImage()