# Read Write Pixel
#   region or single region of interest
#   Interpret part of image
#   Save for analysis
# 3 layers represent bgr channel we change it to rgb

import cv2 as cv
import os
import matplotlib.pyplot as plt

# Reading and writing a single pixel on an image
def readWriteSinglePixel():
    root = os.getcwd()
    imgPath= os.path.join(root, 'Opencv/image/cat.jpeg')
    img = cv.imread(imgPath)

    # BGR -> RGB since matplotlib takers rgb
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    # Accessing eye pixel 
    eyePixel = imgRGB[20, 60]

    # writing to it
    imgRGB[20,60] = (255,0,0)
    debug = 1
    
    plt.figure() # creates a blank canvas
    plt.imshow(imgRGB)
    plt.show()

# access a regoin of image
def readAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Opencv/image/cat.jpeg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    eyeRegion = imgRGB[290:340 , 326:380] # accessing rows and columns
    debug = 1

    dx = 340 - 290
    dy =380 - 326

    StartX = 238
    StartY = 411
    imgRGB[StartX : StartX+dx, StartY : StartY+dy] = eyeRegion

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    # readWriteSinglePixel()
    readAndWritePixelRegion()