#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2
import numpy as np
import random
import time

from paho.mqtt import client as mqtt_client
broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'GB Tech Aeonix_5GHz'
password = 'GBAeo@202'
msg=""
threshold = 150
current_depth = 694
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client,val):
    msg_count = 0
    while True:
        # time.sleep(1)
        result = client.publish(topic, val)
        status = result[0]
        if status == 0:
            print(f"Send `{val}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        return

while (True):
    client = connect_mqtt()
    client.loop_start()
    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth >= current_depth - threshold,
                                 depth <= current_depth + threshold)
    depth = depth.astype(np.uint8)
    # cv2.imshow('Depth', depth)
    depth1=cv2.resize(depth,(20,10))
    val=range(20)
    val2=range(10)
    for i in val:
        for j in val2:
            msg=msg+str(depth1[j,i])+" "
    publish(client,msg)
    cv2.imshow('Dpp',depth1)
    cv2.imshow('Video', frame_convert2.video_cv(freenect.sync_get_video()[0]))
    msg=""
    if cv2.waitKey(10) == 27:
        break
