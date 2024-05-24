"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Data Type ===

BFDSessions	            BFD sessions
BGPNeighbor	            BGP neighbors
Bridge	                Bridge interfaces
ControlConnection	    Active control connections
ControlLocalProperty	Basic configuration parameters and local device properties related to the control plane
ControlWanInterface	    WAN interface control connection information
HardwareAlarms	        Active hardware alarms
HardwareEnvironment	    Status information about router components, including temperature
HardwareInventory	    Inventory of router hardware components, including serial numbers
Interface	            Interface information
OMPPeer	                Active OMP peering sessions
SystemStatus	        Logging, reboot, and configuration history
System	                Summary of general system-wide parameters

URL Format = /dataservice/data/device/state/<data_type>?count=<number_of_query>

"""
import requests
from a_get_login import authenticate
import json
import pprint


vmanage_ip = '192.168.71.80'
api_info = '/dataservice/data/device/state/System'

url = f'https://{vmanage_ip}:443{api_info}'

# === get interface info ===

def get_info():
    session = authenticate()

    response = session.get(url=url,verify=False)
    if response.status_code == 200:
       json_data = response.json()
       for item in json_data['data']:
           print (item)
    else:
        print (f'error is occured : {response.status_code}')
        print (response.content)

get_info()