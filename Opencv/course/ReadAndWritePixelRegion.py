import cv2 as cv
import os
import matplotlib.pyplot as plt

def ShowIMG():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Opencv/image/cat2.jpg')
    img = cv.imread(imgPath)
    # BGR -> RGB 
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # Empty canvas 
    plt.figure()
    plt.imshow(imgRGB) # plotting it on canvas
    plt.show()


def ReadAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Opencv/image/cat2.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#                     row (height) columns(width)
    eyeRegion = imgRGB[500 : 1000, 5 : 1000 ]

    dx = 1000 - 500
    dy = 1000 - 5

    startX = 700
    startY = 893

    imgRGB[startX : startX+dx , startY : startY+dy] = eyeRegion 


    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    # ShowIMG()
    ReadAndWritePixelRegion()
    