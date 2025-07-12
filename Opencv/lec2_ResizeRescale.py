import cv2 as cv

# Rescaling width and height to smaller value since most cam do not support going higher than it

def rescaleFrame(frame, scale=0.75):
    # works for img, vid, live vid
    width = int(frame.shape[1] * scale) # 1 is width
    height = int(frame.shape[0] * scale) # 0 is height
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)
    


# In Image

img = cv.imread('Opencv/image/Anvika.jpg')
Resized_Image = rescaleFrame(img)

cv.imshow('Anvika', Resized_Image)
cv.waitKey(0)

# In Video

capture = cv.VideoCapture('Opencv/image/GUJARIYA.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): ##if d is pressed, stop video
        break

capture.release()

