import paho.mqtt.client as mqtt
import ssl
import json


class MQTTClient(object):
    def __init__(self, host, port):
        # Initialize MQTT client.
        self._client = mqtt.Client()
        self.host = host
        self.port = port
        self.topic = None
        self.on_message = None
        self.msg_topic = None
        self.msg_payload = None
        self.msg = []
        self._client.on_connect = self.on_connect
        self._client.on_disconnect = self.disconnect
        self._client.on_message = self._on_message
        self._client.on_log = self.on_log
        self._connected = False

    def tls_set(self, ca_certs=None, certfile=None, keyfile=None, cert_reqs=None, tls_version=None, ciphers=None):
        self._client.tls_set(ca_certs, certfile, keyfile, tls_version=ssl.PROTOCOL_TLSv1_2)
        self._client.tls_insecure_set(True)
        print("ca_certs ......")

    def connect(self, username, password):
        ssl.match_hostname = lambda cert, hostname: True
        self._client.username_pw_set(username, password)
        self._client.connect(self.host, self.port, 60)
        print(username,"\n", self.host)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        if rc == 0:
            self._connected = True

    def disconnect(self):
        self._client.disconnect()

    def _on_message(self, client, userdata, msg):
        # print(msg.topic+" "+str(msg.payload))
        self.msg_topic = msg.topic
        self.msg_payload = json.loads(msg.payload.decode("utf-8"))
        print("\n\n\n", self.msg_payload)
        self.msg_payload['sub_topic'] = self.msg_topic
        self.msg.append(self.msg_payload)
        with open ("nome_sub_info.json", "a") as dump_f:
            json.dump(self.msg_payload, dump_f, indent=4, ensure_ascii=False)
        return self.msg_payload
        # self.on_message(self, msg.topic, str(msg.payload))
        # print(self.msg_topic)
        # print(self.msg_payload)

    def loop(self, timeout_sec=0.5):
        self._client.loop_forever()
        # self._client.loop(timeout=timeout_sec)

    def loop_start(self):
        self._client.loop_start()

    def loop_stop(self):
        self._client.loop_stop()

    def is_connected(self):
        return self._connected

    def subscribe(self, topic):
        self.topic = topic
        self._client.subscribe(self.topic)
        print(self.topic)
        # self.msg = []

    def unsubscribe(self):
        self._client.unsubscribe(self.topic)

    def on_publish(self, topic, payload, qos):
        self._client.publish(topic, payload, qos)

    def clear_msg(self):
        self.msg = []

    def clear_all(self):
        self.topic = None
        self.msg_topic = None
        self.msg_payload = None
        self.msg = []

    def on_log(self, mqttc, obj, level, string):
        print(level, string)
