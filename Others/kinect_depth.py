#!/usr/bin/env python3
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2  
import numpy as np

while(True):
    (depth,_), (frame,_) = get_depth(), get_video()
    frame=cv2.flip(frame,1)
    frame1 = cv2.resize(frame, (20,10))
    con=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
    da = np.hstack((d3,frame))
    np.clip(depth, 0, 2**9.5-1, depth)
    depth1 = depth.astype(np.uint8)
    cv2.imshow("Frame", con)
    cv2.imshow("Frame1", frame)
    cv2.imshow('both',np.array(da[::2,::2,::-1]))
    cv2.imshow('depth',depth1)

    # print (depth)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
# cap.release()
cv2.destroyAllWindows()

# def doloop():
#     global depth, rgb
#     while True:
#         # Get a fresh frame
#         (depth,_), (rgb,_) = get_depth(), get_video()
        
#         # Build a two panel color image
#         d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
#         da = np.hstack((d3,rgb))
        
#         # Simple Downsample
#         cv.imshow('both',np.array(da[::2,::2,::-1]))
#         cv.WaitKey(5)
        
# doloop()

# cap = cv2.VideoCapture(0)
# greenLower = (29, 86, 6)
# greenUpper = (64, 255, 255)
# orangeLower =(0, 100, 20)
# orangeUpper= (10, 255, 255)

