#!/usr/bin/python3

import cv2

from picamera2 import Picamera2

# Grab images as numpy arrays and leave everything else to OpenCV.

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while True:
    im = picam2.capture_array()
    frame=cv2.flip(im,1)
    frame=cv2.resize(frame,(12,4))

    con = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", con)