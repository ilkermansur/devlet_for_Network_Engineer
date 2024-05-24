"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Get Device Info ARGs===


"""
import requests
import json
from a_get_login import authenticate

vmanage_ip = '192.168.71.80'
session = authenticate()
base_url = f"https://{vmanage_ip}:443"
api_device = '/dataservice/device'

# Function to get device information
def get_devices():
    response = session.get(url=base_url+api_device,
                           verify=False)
    if response.status_code == 200:
        devices = response.json()['data']
        print (json.dumps(devices, indent=4))
        return devices
    else:
        print("Failed to get device information")
        exit()

get_devices()

