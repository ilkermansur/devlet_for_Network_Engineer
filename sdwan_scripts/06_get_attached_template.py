"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur
"""

import requests
from a_get_login import authenticate
import json
import pprint

vmanage_ip_address = '192.168.71.80'
device_id = 'C1117-4PLTEEA-FCZ241392GH'
api_template = f'/dataservice/template/config/attached/{device_id}'

# === get devices ===

def get_attached_template():
    session = authenticate()
    url_device = f'https://{vmanage_ip_address}:443{api_template}'

    response = session.get(url=url_device,verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()['config']
        print(data)
    
    else:
        print (f"Get Devices Failed : {response.content}")


get_attached_template()