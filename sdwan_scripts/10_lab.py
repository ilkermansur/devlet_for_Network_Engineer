"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur
"""

import requests
import json

"""
== LAB ==

1- Get all templates and its ID's                                       # get_templates()
2- Get ID of the device to which you want to attach the template        # get_devices()
3- Generate Device Input Variables                                      # generate_device_variable()
4- Fill the template and generate template preview                      # generate_template_preview()
5- Attached template to device                                          # attached_template()
6- Check status                                                         # attached_status()
"""

vmanage_ip_address = '192.168.71.80'
username = 'admin'
password = 'admin123'
api_connect = 'j_security_check'

sec_payload = {
    'j_username': username,
    'j_password': password
}
requests.packages.urllib3.disable_warnings()

# === login to vManage ===

def login_vmanage():
    url = f'https://{vmanage_ip_address}:443/{api_connect}'
    session = requests.session()
    response = session.post(url=url, data=sec_payload, verify=False)
    if response.status_code == 200 :
        print (f"Login Success")
    else :
        print (f"Login Failed {response.status_code}")
        print (response.content)
        
    return session

# === get token ===

api_token = 'dataservice/client/token'

url_token = f'https://{vmanage_ip_address}:443/{api_token}'

def getting_token():
    session = login_vmanage()
    response = session.get(url=url_token,verify=False)

    if response.status_code == 200:
        print ("Getting Token Success")
        token = response.content.decode('ascii')
        headers = {'X-XSRF-TOKEN': token}

        # add token to session header
        session.headers.update(headers)

    else:
        print (f"Getting Token Failed : {response.content}")

    return session

# ============ STEP - 1 ============ 

# get templates

def get_templates():
    api_templates = '/dataservice/template/device'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.get(url=url_device,verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()['data']
        print(json.dumps(data, indent=4))
    
    else:
        print (f"Get Devices Failed : {response.content}")

# get_templates()

"""
[
--- ommited output ---
 {
        "deviceType": "vedge-C1111X-8P",
        "lastUpdatedBy": "admin",
        "resourceGroup": "global",
        "templateClass": "cedge",
        "configType": "file",
        "templateId": "11e21206-d820-41f7-a6f4-41a92904b335", <-- Temp ID -->
        "factoryDefault": false,
        "templateName": "Demo-Template-ilkerM",
        "devicesAttached": 0,
        "templateDescription": "Demo-Template-ilkerM",
        "draftMode": "Disabled",
        "lastUpdatedOn": 1716387524411,
        "templateAttached": 0
    }
--- ommited output ---
]
"""

# ============ STEP - 2 ============ 

def get_devices():
    api_templates = '/dataservice/device'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.get(url=url_device,verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()['data']
        print(json.dumps(data, indent=4))
    
    else:
        print (f"Get Devices Failed : {response.content}")

# get_devices()

"""
--- ommited output ---
 {
        "deviceId": "100.255.34.1",
        "system-ip": "100.255.34.1",
        "host-name": "IST-BRANCH-1-R1",
        "reachability": "reachable",
        "status": "normal",
        "personality": "vedge",
        "device-type": "vedge",
        "timezone": "UTC +0000",
        "device-groups": [
            "No groups"
        ],
        "lastupdated": 1716385384154,
        "bfdSessionsUp": 3,
        "domain-id": "1",
        "board-serial": "01939A67",
        "certificate-validity": "Valid",
        "max-controllers": "0",
        "uuid": "C1111X-8P-FGL231914C6",        <-- UUID of device -->
        "bfdSessions": "3",
        "controlConnections": "3",
        "device-model": "vedge-C1111X-8P",
        "version": "17.12.01a.0.118",
        "connectedVManages": [
            "10.255.34.1"
        ],
        "site-id": "34005",
        "ompPeers": "1",
        "latitude": "37.666684",
        "longitude": "-122.777023",
        "isDeviceGeoData": false,
        "platform": "x86_64",
        "uptime-date": 1714036080000,
        "statusOrder": 4,
        "validity": "valid",
        "state": "green",
        "state_description": "All daemons up",
        "model_sku": "None",
        "local-system-ip": "100.255.34.1",
        "total_cpu_count": "4",
        "linux_cpu_count": "2",
        "testbed_mode": false,
        "layoutLevel": 4,
        "site-name": "SITE_34005"
    },
--- ommited output ---
"""

# ============ STEP - 3 ============ 

data_input = {
  "templateId":"16faea96-fb79-4085-9d4a-0b76a89cb590",  
  "deviceIds":
    [                    
      "C1111X-8P-FGL231914C6"
    ],
  "isEdited":False,        
  "isMasterEdited": False           
  }

def generate_device_variable():
    api_templates = '/dataservice/template/device/config/input'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.post(url=url_device, data = json.dumps(data_input), verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()['data']
        print(json.dumps(data, indent=4))
    
    else:
        print (f"Get Devices Failed : {response.content}")

# generate_device_variable()

"""
[
    {
    {
        "csv-status": "in_complete",
        "csv-deviceId": "C1111X-8P-FGL231914C6",
        "csv-deviceIP": "100.255.34.1",
        "csv-host-name": "IST-BRANCH-1-R1",
        "hostname": ""
    }
    }
]
"""

# ============ STEP - 4 ============ 

payload = {
  "templateId": "16faea96-fb79-4085-9d4a-0b76a89cb590",
  "device": {
        "csv-status": "in_complete",
        "csv-deviceId": "C1111X-8P-FGL231914C6",
        "csv-deviceIP": "100.255.34.1",
        "csv-host-name": "IST-BRANCH-1-R1",
        "hostname": "IST-BR-1-Router-01"
    },
  "isEdited": False,
  "isMasterEdited": False
}

def generate_template_preview():
    api_templates = '/dataservice/template/device/config/config'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.post(url=url_device, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        print (response.text)
    
    else:
        print (f"Get Devices Failed : {response.content}")

# generate_template_preview()

"""
--- ommited output ---
  hostname IST-BR-1-Router-01 <-- Change variable -->
--- ommited output ---
"""

# ============ STEP - 5 ============

payload = {
  "deviceTemplateList":[
      {
  "templateId": "16faea96-fb79-4085-9d4a-0b76a89cb590",
  "device": [
      {
        "csv-status": "in_complete",
        "csv-deviceId": "C1111X-8P-FGL231914C6",
        "csv-deviceIP": "100.255.34.1",
        "csv-host-name": "IST-BRANCH-1-R1",
        "hostname": "IST-BR-1-Router-01"
    }
  ],
  "isEdited": False,
  "isMasterEdited": False
}
  ]
}

def attached_template():
    api_templates = '/dataservice/template/device/config/attachcli'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.post(url=url_device, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        print (response.text)
    
    else:
        print (f"Get Devices Failed : {response.content}")

# attached_template()

"""
{"id":"push_file_template_configuration-038bac14-6991-4ea7-bfef-0fa8226e0468"}
"""
# ============ STEP - 6 ============

id = "push_file_template_configuration-8daf6101-15b2-4c20-9e60-4c89025cc1ff"

def attached_status():
    api_templates = f'/dataservice/device/action/status/{id}'
    session = getting_token()
    url_device = f'https://{vmanage_ip_address}:443{api_templates}'

    response = session.get(url=url_device, verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()
        print (json.dumps(data['data'], indent=4))
    
    else:
        print (f"Get Devices Failed : {response.content}")

attached_status()
