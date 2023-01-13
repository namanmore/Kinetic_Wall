# 150 threshold
# 694 depth
#!/usr/bin/env python3
import cv2
import time
import smbus   #i2c library(can use with laptop too)
import time
# from picamera2 import Picamera2
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
num=range(16)
for i in num:
    bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_START[i], 0)  # 0us
    bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_START[i], 0)  # 0us
    bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_START[i], 0)  # 0us
# Set channel start times


# image = cv2.imread("pic.png")
# ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
# height, width = image.shape[:2]
# w, h = (12, 4)
# temp = cv2.resize(thresh1, (w, h), interpolation=cv2.INTER_LINEAR)
# output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
# frame2=cv2.resize(image,(12,4))
# cv2.imshow("a",output )



cv2.startWindowThread()
# picam2 = Picamera2()
# picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (1200, 400)}))
# picam2.start()
while True:
    # im = picam2.capture_array()
    # frame = cv2.flip(im,1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,frame1=cv2.threshold(frame, 50, 255, cv2.THRESH_BINARY)
    height, width = frame.shape[:2]
    w, h = (12, 4)
    temp = cv2.resize(frame1, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    frame2=cv2.resize(output,(12,4))
    val=range(12)
    val2=range(4)
    print(frame2)
    i=0
    for m in val:
        for n in val2:
            z=int(frame2[n,m])
#             print(z,end=" ")
            if (i<16):
                if(z<100):
                    bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_END[i], b_ang) #0 degrees
                else:
                    bus.write_word_data(BOARD1_I2C_ADDR, CHANNEL_END[i], w_ang) #90 degrees
            if (i>15 and i<32):
                if(z<100):
                    bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_END[i-16], b_ang)
                else:
                    bus.write_word_data(BOARD2_I2C_ADDR, CHANNEL_END[i-16], w_ang)
            if (i>31 and i<48):
                if(z<100):
                    bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_END[i-32], b_ang) #0 degrees
                else:
                    bus.write_word_data(BOARD3_I2C_ADDR, CHANNEL_END[i-32], w_ang)
            i+=1
#         print()        
    i=0
    cv2.imshow('Output', output)
    cv2.imshow('Real',frame)
    print("##########")
cv2.waitKey(0)
