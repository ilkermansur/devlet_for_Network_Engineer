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

# === get templates ===

api_templates = '/dataservice/template/device'

def get_templates():
    session = authenticate()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.get(url=url_device,verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()['data']
        print(json.dumps(data, indent=4))
    
    else:
        print (f"Get Devices Failed : {response.content}")


get_templates()