from mqtt_client import MQTTClient
import ssl
import json
import paho.mqtt.client as mqtt


with open ("config/config.json", "r") as load_f:
    parameter = json.load(load_f)

cli = MQTTClient(parameter["host"], parameter["port"])

cli.tls_set(parameter["ca_cert"], parameter["certfile"], parameter["keyfile"])

cli.on_log

cli.connect(parameter["username"], parameter["password"])

cli.on_connect

cli.subscribe(parameter["topic0"])

cli._on_message

cli.loop()
