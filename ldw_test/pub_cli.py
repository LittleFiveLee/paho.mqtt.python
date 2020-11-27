#!/usr/bin/python

#!/usr/bin/python

import sys
import datetime
import socket, sys
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    pass
def transmitMQTT(strMsg):
    host = "127.0.0.1"
    port = 1883
    topic = "test"
    print(strMsg)
    ser = mqtt.Client()
    ser.connect(host, port)
    ser.publish(topic, "hello 十八子李",0)
    # print(ser.msg)
    # ser.loop_forever()

if __name__ == '__main__':
    transmitMQTT("Hello,MQTT")
    print ("Send msg ok.")
