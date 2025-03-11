import swagger_controller as sc
import json
import time
import os
import random

api_key = "APIKEY"

json_string = """{
    "workCenterId": "1",
    "quantity": 0,
    "countType": "GoodCount",
    "reasonId": "Produzindo",
    "fromDevice": true,    
    "userId": "bruno.jesus@ic.ufal.br"
}
"""


fault_paths = ["array_faults", "boolean_faults", "number_faults", "string_faults", "date_faults", "datetime_faults"]
for path in fault_paths:
    mutated_jsons = os.listdir(path)
    for json_file_path in mutated_jsons:
        if json_file_path != ".gitkeep":
            json_file = open(path + "\\" + json_file_path)
            json_data = json.load(json_file)
            print(f"\n _________________ \n FAULT GROUP: {path}. MUTATED JSON: {json_file_path} \n _________________ \n\n  ")
            json_data = json.dumps(json_data, indent=4)
            r = sc.send_json(json_data, api_key, 10)
            time.sleep(1)
