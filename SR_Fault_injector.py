# import pandas as pd
import json
import paho.mqtt.client as mqtt
import time
import os
import random

broker_address = "mqtt.thingsboard.cloud"
port = 1883
topic = "v1/devices/me/telemetry"
def send_via_mqtt(json_data):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "control1")
    client.username_pw_set("PASSKEY", "")
    client.connect(broker_address, port)
    client.loop_start()
    r = client.publish(topic, json.dumps(json_data, indent=4, sort_keys=True, default=str))
    time.sleep(1)
    client.loop_stop()
    client.disconnect()
    return r

def send_correct_values(num):
    for i in range(num):
        with open("sr_base_payload.json", "r") as f:
            dados = json.load(f)
        dados["ph"] = random.randint(6, 8)
        dados["temperature"] = random.randint(22, 30)
        with open("sr_base_payload.json", "w") as f:
            json.dump(dados, f, indent=4)
        json_file = open("sr_base_payload.json")
        json_data = json.load(json_file)
        send_via_mqtt(json_data)
        

fault_paths = ["array_faults", "boolean_faults", "number_faults", "string_faults", "date_faults", "datetime_faults"]
for path in fault_paths:
    mutated_jsons = os.listdir(path)
    for json_file_path in mutated_jsons:
        if json_file_path != ".gitkeep":
            json_file = open(path + "\\" + json_file_path)
            json_data = json.load(json_file)
            send_correct_values(12)
            print(f"\n _________________ \n FAULT GROUP: {path}. MUTATED JSON: {json_file_path} \n _________________ \n  ")
            r = send_via_mqtt(json_data)
            time.sleep(1)
