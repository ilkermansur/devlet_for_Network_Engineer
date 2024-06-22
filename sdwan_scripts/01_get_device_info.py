"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Example Output ===

{
        "deviceId": "100.255.35.1",
        "system-ip": "100.255.35.1",
        "host-name": "IZM-BRANCH-1-R1",
        "reachability": "unreachable",
        "status": "normal",
        "personality": "vedge",
        "device-type": "vedge",
        "timezone": "UTC +0000",
        "device-groups": [
            "No groups"
        ],
        "lastupdated": 1718345422380,
        "bfdSessionsUp": 0,
        "domain-id": "1",
        "board-serial": "0193041F",
        "certificate-validity": "Valid",
        "max-controllers": "0",
        "uuid": "C1111X-8P-FGL231912KY",
        "bfdSessions": "--",
        "controlConnections": "--",
        "device-model": "vedge-C1111X-8P",
        "version": "17.12.01a.0.118",
        "connectedVManages": [],
        "site-id": "35005",
        "ompPeers": "--",
        "latitude": "37.666684",
        "longitude": "-122.777023",
        "isDeviceGeoData": false,
        "platform": "x86_64",
        "uptime-date": 1715929680000,
        "statusOrder": 4,
        "validity": "valid",
        "state": "green",
        "state_description": "All daemons up",
        "model_sku": "None",
        "local-system-ip": "100.255.35.1",
        "total_cpu_count": "4",
        "linux_cpu_count": "2",
        "testbed_mode": false,
        "layoutLevel": 4,
        "site-name": "SITE_35005"
    },

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

