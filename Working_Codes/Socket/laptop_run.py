#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2   # The file present in the same directory as this
import numpy as np
import random
import time
import socket
import pickle 
HOST = '0.0.0.0'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ("Connected by", addr)
msg=":"
threshold = 150   # threshold for kinect depth
current_depth = 694 # depth control for kinect    Refer kinect_depth_control code to get the desired values
while (True):
    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth >= current_depth - threshold,
                                 depth <= current_depth + threshold)
    depth = depth.astype(np.uint8)
    depth = cv2.flip(depth,1)
    ret,depth1=cv2.threshold(depth,0,255,cv2.THRESH_BINARY)
    # depth1=depth
    height,width=depth.shape[:2]
    w,h=(4,10)  # w-> number of pixels in horizontal/width simply. h->number of pixels in vertical/height simply 
    temp=cv2.resize(depth1,(w,h),interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    # depth1=cv2.resize(depth,(20,10))
    output = cv2.fastNlMeansDenoising(output, None, 20, 7, 21) 
    frame2=cv2.resize(output,(4,10))   #resize according to the pixel(w,h)
    val=range(4)        # pixels in WIDTH
    val2=range(10)      # pixels in HEIGHT
    for i in val:
        for j in val2:
            msg=msg+str(frame2[j,i])+":"
    conn.send(msg.encode())
    cv2.imshow('Depth', depth)    
    cv2.imshow('Output',output)
    cv2.imshow('Video', frame_convert2.video_cv(freenect.sync_get_video()[0]))
    print(msg)
    msg=":"
    if cv2.waitKey(10) == 27: 
        break
conn.close()

