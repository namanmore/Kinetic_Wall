#!/usr/bin/python3
import cv2
import time
import smbus
import time
import socket, pickle
import numpy as np
from picamera2 import Picamera2
BOARD1_I2C_ADDR = 0x40
BOARD2_I2C_ADDR = 0x41
BOARD3_I2C_ADDR = 0x42
CHANNEL_START=[None]*16
CHANNEL_END=[None]*16
num=range(15)   
#305 90 degrees
w_ang=210 #45degrees
b_ang=115 #0degrees
CHANNEL_START[0]=0x06
CHANNEL_END[0]=0x08


for i in num:
    CHANNEL_START[i+1]=CHANNEL_START[i]+ 0x4
    CHANNEL_END[i+1]=CHANNEL_END[i]+ 0x4
MODE1_REG_ADDR = 0
PRE_SCALE_REG_ADDR = 0xFE
bus = smbus.SMBus(1)
# Enable prescaler change
bus.write_byte_data(BOARD1_I2C_ADDR, MODE1_REG_ADDR, 0x10)
bus.write_byte_data(BOARD2_I2C_ADDR, MODE1_REG_ADDR, 0x10)
bus.write_byte_data(BOARD3_I2C_ADDR, MODE1_REG_ADDR, 0x10)

# Set prescaler to 50Hz from datasheet calculation
bus.write_byte_data(BOARD1_I2C_ADDR, PRE_SCALE_REG_ADDR, 0x80)
bus.write_byte_data(BOARD2_I2C_ADDR, PRE_SCALE_REG_ADDR, 0x80)
bus.write_byte_data(BOARD3_I2C_ADDR, PRE_SCALE_REG_ADDR, 0x80)

time.sleep(.25)

# Enable word writes
bus.write_byte_data(BOARD1_I2C_ADDR, MODE1_REG_ADDR, 0x20)
bus.write_byte_data(BOARD2_I2C_ADDR, MODE1_REG_ADDR, 0x20)
bus.write_byte_data(BOARD3_I2C_ADDR, MODE1_REG_ADDR, 0x20)

i=0
num=range(16)  # Will be fixed as one Servo Driver has 16 channels, hence 0 to 15
for i in num:
    bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_START[i], 0)  # 0us
    bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_START[i], 0)  # 0us
    bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_START[i], 0)  # 0us


HOST = '192.168.5.97'    # IP of the laptop from where the kinect data is being sent
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr=np.zeros((4,10),np.uint8)      # (width,height) change accordingly

while True:
    data = s.recv(40960)
    values=data.decode()
    foo=values.split(":")
    foo.pop()
    print("start")
    if (len(foo)==41):
    #     arr=np.array(foo,np.uint8)
        shape = (10,4)            # (height,width) change accordingly
    #     arr=arr.reshape(shape)
        for i in range(1,len(foo)):
            if(foo[i]!=''):
                foo[i]=int(foo[i])       # convert all the values received from str class to int 
        print(foo)
    #     cv2.namedWindow('Output')
    #     cv2.imshow('Output', arr)
    #     cv2.imshow('Real',frame)
    #     print("##########")
    #     cv2.waitKey(27)
        val=range(4)          # pixels in WIDTH
        val2=range(10)        # pixels in HEIGHT
    #     print(frame2)
        i=0
        j=1
        
        for m in val:
            for n in val2:
                z=int(foo[j])
    #             print(z,end=" ")              # get each pixel value in z         
                if (i<16):                      # checking if all servos from first driver have been actuated 
                    if(z<100):
                        bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_END[i], w_ang) #90 degrees
                    elif(z>200):
                        bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_END[i], b_ang) #0 degrees
                if (i>15 and i<32):
                    if(z<100):
                        bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_END[i-16], w_ang)
                    elif(z>200):
                        bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_END[i-16], b_ang)
                if (i>31 and i<48):
                    if(z<100):
                        bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_END[i-32], w_ang) #90 degrees
                    elif(z>200):
                        bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_END[i-32], b_ang)
                i+=1
                j+=1
        i=0
        j=1
cv2.waitKey(0)
s.close()
