"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Get Alarms ARGs ===
vmanage_ip = '192.168.71.80'


"""
import requests
import json
from a_get_login import authenticate

vmanage_ip = '192.168.71.80'

# Getting session from `get_login.py`
session = authenticate()

pre_payload = {
	"size": 100, # Return 100 records
	"query": {
		"condition": "OR", # Records must match all rules; there are three:
		"rules": [
				{
				"value": [
				"24" # Rule #1: Records from the last 24 hours
					],
				"field": "entry_time",
				"type": "date",
				"operator": "last_n_hours"
				},
				{
				"value": [
				"critical" # Rule #2: Severity level = critical
					],
				"field": "severity_level",
				"type": "string",
				"operator": "in"
				},
				{
				"value": [
				"security" # <== Rule #3: Event type = security
					],
				"field": "component",
				"type": "string",
				"operator": "in"
				}
			]
		}
	}

api_alarms = f'/dataservice/alarms?query={json.dumps(pre_payload)}'
base_url = f"https://{vmanage_ip}:443"

def get_alarms():
        response = session.get(url=base_url+api_alarms,verify=False)
        if response.status_code == 200:
            list_data = list(response.json()['data'])
            for alarm in list_data :
                print ('=' * 100)
                print (json.dumps(alarm, indent=4))
        else:
            print (f'error is occured : {response.status_code}')
            print (response.content)

get_alarms()


