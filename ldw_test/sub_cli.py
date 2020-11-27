import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 1883
topic = "test"
cli = mqtt.Client("ttt")
cli.connect(host,port)
cli.subscribe(topic)

def on_message(client, userdata, msg):
    print("***" + msg.topic+" "+ str(msg.qos) + " " + msg.payload.decode("utf-8"))

cli.on_message = on_message
cli.loop_forever()
