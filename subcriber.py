import paho.mqtt.client as mqtt
import logging


def on_connect(_client, _userdata, _flags, rc):
    logging.info(f"Connected with result code {str(rc)}")
    client.subscribe("SRIJAN")


def on_message(_client, _userdata, msg):
    logging.info(f"Received message: {str(msg.payload.decode())}")


logging.basicConfig(level=logging.INFO)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 61)
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
