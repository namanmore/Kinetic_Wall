#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2
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
msg=""
threshold = 150
current_depth = 694
while (True):
    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth >= current_depth - threshold,
                                 depth <= current_depth + threshold)
    depth = depth.astype(np.uint8)
    depth1=cv2.resize(depth,(20,10))
    val=range(20)
    val2=range(10)
    for i in val:
        for j in val2:
            msg=msg+str(depth1[j,i])+":"
    conn.send(msg.encode())
    cv2.imshow('Dpp',depth1)
    cv2.imshow('Video', frame_convert2.video_cv(freenect.sync_get_video()[0]))
    msg=""
    if cv2.waitKey(10) == 27:
        break
conn.close()
