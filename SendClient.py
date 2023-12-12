from paho.mqtt import client as mqtt_client
import json
import random
import time

broker = 'localhost'
port = 1883
topic = 'uam/salones'
client_id = f'pyhon-mqtt-{random.randint(0,100)}'

profesores = ['Juan', 'Raymundo', 'Beatriz', 'Joaquin']
nombresSalones = ['']

class Salon:
    edificio = "G"
    salon = '202'
    temperatura = 32
    humedad = "50"
    luminosidad = 0
    person = "Joaquin"
    reconocido = 0
    rfid = '00'
    count = 0

def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    salon1 = Salon()
    salon1.person = "Joaquin"
    salon1.count = 0
    salon2 = Salon()
    salon2.person = "Beatriz"
    salon2.count = 0
    salon3 = Salon()
    salon3.person = "Rafael"
    salon3.count = 0
    while True:
        salon1.edificio = "G"
        salon1.salon = "103"
        salon1.temperatura = random.randint(20,32)
        salon1.luminosidad = random.randint(0,1)
        salon1.reconocido = random.randint(0,1)
        salon1.rfid = 'AB-CD-EF-GH'
        salon2.edificio = "G"
        salon2.salon = "203"
        salon2.temperatura = random.randint(20,32)
        salon2.luminosidad = random.randint(0,1)
        salon2.reconocido = random.randint(0,1)
        salon2.rfid = 'IJ-KL-MN-OP'
        salon3.edificio = "W"
        salon3.salon = "302"
        salon3.temperatura = random.randint(20,32)
        salon3.luminosidad = random.randint(0,1)
        salon3.reconocido = random.randint(0,1)
        salon3.rfid = 'IJ-KL-MN-OP'
        time.sleep(5)
        msgs = []
        msgs.append(json.dumps(salon1.__dict__))
        msgs.append(json.dumps(salon2.__dict__))
        msgs.append(json.dumps(salon3.__dict__))
        topics = ["G202", "G203", "G102"]
        for x, msg in zip(topics, msgs):    
            result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send '{msg}' to topic salones")
        else:
            print(f"Failed to send message to topic salones")
        salon1.count += 1
        salon2.count += 1
        salon3.count += 1

def run():
    client = connect()
    client.loop_start()
    publish(client)

if __name__ == "__main__":
    run()
