import cv2 as cv

# Reading Image
img = cv.imread('Opencv/image/Anvika.jpg')
cv.imshow('Anvika', img)
cv.waitKey(0)

img2 = cv.imread('Opencv\image\cat.jpeg')
cv.imshow('cat', img2)
cv.waitKey(0)

# Reading Video
# cv.VideoCapture takes integer or path

capture = cv.VideoCapture('Opencv/image/GUJARIYA.mp4') # reads a video

while True:
    isTrue, frame = capture.read() # read a single frame
    
    cv.imshow('Video', frame) # Shows frames simultaneously

    if cv.waitKey(20) & 0xFF==ord('d'): ##if d is pressed, stops video
        break

capture.release()