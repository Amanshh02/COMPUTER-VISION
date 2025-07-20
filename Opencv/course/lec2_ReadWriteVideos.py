# Video with frames. each frame is a component of video
# Why read/write??
    # to interpret something in video
    # save for preprocessing and analysis
# each frame has channel which are set of three.
# matrix is passed

import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

# reading to webcam 
def videoFromWebcam() :
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()
    
    while True :
        ret, frame= cap.read()
        if ret:
            cv.imshow('webcam', frame)

        if cv.waitKey(1) == ord('q'):
            break        

# Read video from file
def videoFromFile():
    root = os.getcwd()
    videoPath = os.path.join(root, 'Opencv/videos/2024-10-07 01-59-26.mp4')
    cap = cv.VideoCapture(videoPath)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break

# Write video to file
def writeVideoToFile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd()
    outputPath = os.path.join(root, 'Opencv/videos//webcam.mov')
    out = cv.VideoWriter(outputPath, fourcc, 30.0, (640,450)) # 20fps, 640x40 is frame size

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            out.write(frame)
            cv.imshow('Webcam', frame)

            if cv.waitKey(1) == ord('q'):
                    break
    cap.release()
    out.release()

if __name__ == '__main__':
    # videoFromWebcam()
    # videoFromFile()
    writeVideoToFile()

