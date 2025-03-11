import os
import fault_model as fm
import json

def clean_dir(path):
    files = os.listdir(path)
    for file in files:
        if (file != ".gitkeep"): 
            os.remove(path+"/"+file)

def convert_date_time_pt(datetime_string):
    if (datetime_string != "") and (datetime_string != None):
        date, time = datetime_string.split(" ")
        year, month, day = date.split("-")
        datetime_string = day + "/" + month + "/" + year + " " + time
    return datetime_string

def convert_date_time_us(datetime_string):
    if (datetime_string != "") and (datetime_string != None):
        date, time = datetime_string.split(" ")
        day, month, year = date.split("/")
        datetime_string = year + "-" + month + "-" + day + " " + time
    return datetime_string


clean_dir("./array_faults")
clean_dir("./boolean_faults")
clean_dir("./number_faults")
clean_dir("./string_faults")
clean_dir("./date_faults")
clean_dir("./datetime_faults")

# fault_dicts = [fm.array_faults, fm.boolean_faults, fm.number_faults, fm.string_faults, fm.date_faults, fm.datetime_faults]
# json_field_groups = [["array"], ["boolean"], ["number_int32", "number_int64", "number_float", "number_double"], ["string_password"], ["string_date"], ["string_datetime"]]
# fault_paths = ["array_faults", "boolean_faults", "number_faults", "string_faults", "date_faults", "datetime_faults"]

# WE NEED TO CREATE THE BASE_PAYLOAD FILENAME AND THE 3 LISTS BELOW FOR EACH SUT. 

# BASE_PAYLOAD = "sr_base_payload.json"
# BASE_PAYLOAD = "MInA_base_payload.json"
# BASE_PAYLOAD = "MQTT_base_payload.json"
BASE_PAYLOAD = "STOMP_base_payload.json"
# BASE_PAYLOAD = "AMQP_base_payload.json"

# SMARTRURAL
# fault_dicts = [fm.number_faults]
# json_field_groups = [["ph", "temperature"]]
# fault_paths = ["number_faults"]

# MInA
# fault_dicts = [fm.boolean_faults, fm.number_faults, fm.string_faults]
# json_field_groups = [["fromDevice"],["quantity"],["reasonId","workCenterId", "userId", "countType"]]
# fault_paths = ["boolean_faults", "number_faults", "string_faults"]

# # MQTT
# fault_dicts = [fm.boolean_faults, fm.number_faults, fm.string_faults]
# json_field_groups = [["retain"],["port","qos"],["broker", "topic", "payload"]]
# fault_paths = ["boolean_faults", "number_faults", "string_faults"]

# STOMP
fault_dicts = [fm.boolean_faults, fm.number_faults, fm.string_faults]
json_field_groups = [["persistent"],["port"],["broker", "destination", "payload", "login", "passcode", "priority", "content-type"]]
fault_paths = ["boolean_faults", "number_faults", "string_faults"]  

# # AMQP
# fault_dicts = [fm.number_faults, fm.string_faults, fm.datetime_faults]
# json_field_groups = [["priority"],["broker", "queue", "content_type", "message_type", "user_id", "payload"],["timestamp"]]
# fault_paths = ["number_faults", "string_faults", "datetime_faults"]


for fault_dict, field_group, fault_path in zip(fault_dicts, json_field_groups, fault_paths): 
    for fault in fault_dict.keys(): 
        for field in field_group:
            base_payload = open(BASE_PAYLOAD)
            json_payload = json.load(base_payload)
            print("CREATING SCENARIO {}. TYPE: {} ...".format(fault, field))
            base_value = json_payload[field]
            if fault_path == "datetime_faults":
                base_value = convert_date_time_pt(base_value)
            faulty_value = fault_dict[fault](base_value)
            if fault_path == "datetime_faults":
                faulty_value = convert_date_time_us(faulty_value)
            json_payload[field] = faulty_value
            string_json = json.dumps(json_payload, indent=4, sort_keys=True, default=str) 
            json_file = open("./{}/{}_{}.json".format(fault_path, field, fault),"a")
            json_file.write(string_json)
            json_file.close()