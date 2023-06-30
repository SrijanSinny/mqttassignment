import paho.mqtt.client as mqtt
import logging
import time


def on_connect(_client, _userdata, _flags, rc):
    logging.info(f"connected with result code {str(rc)}")


logging.basicConfig(filename='pub.log', level=logging.DEBUG)
client = mqtt.Client()
client.on_connect = on_connect
# client.on_message = on_message

client.connect("localhost", 1883, 61)
client.loop_start()

while True:
    try:
        message = input("Enter a message to publish (or 'q' to quit): ")
        if message.lower() == 'q':
            break
        client.publish("SRIJAN", message)
        time.sleep(10)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
client.loop_stop()
client.disconnect()

