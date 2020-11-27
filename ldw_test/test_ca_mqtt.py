#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import ssl
# import context  # Ensures paho is in PYTHONPATH


ssl.match_hostname = lambda cert, hostname: True

host = "106.75.225.39"
port = 31731
username = "compass"
password = "compass"
topic = "/efence_k8s_backend/tracking"
topic1 = "/efence_k8s_backend/source_nome"

# tls_set(ca_certs="/opt/certs/root_cert.crt",certfile="/opt/certs/device_cert.crt",keyfile="/opt/certs/device_key.pem",tls_version=ssl.PROTOCOL_TLSv1_2)


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload.decode("utf-8")))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.tls_set(ca_certs="/opt/certs/root_cert.crt",certfile="/opt/certs/device_cert.crt",keyfile="/opt/certs/device_key.pem",tls_version=ssl.PROTOCOL_TLSv1_2)
# mqttc.tls_insecure_set(False)

# Uncomment to enable debug messages

mqttc.username_pw_set(username, password)

mqttc.connect(host, port, 60)
# mqttc.on_connect
mqttc.on_connect = on_connect
mqttc.subscribe(topic1, 0)

mqttc.on_message = on_message
mqttc.on_log = on_log
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe
mqttc.loop_forever()