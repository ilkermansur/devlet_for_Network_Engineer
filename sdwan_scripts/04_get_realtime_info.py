"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

BGP                     /dataservice/device/bgp/summary?deviceId=deviceId
Control                 /dataservice/device/control/connections?deviceId=deviceId
Crash Log               /dataservice/device/crashlog?deviceId=deviceId
DHCP                    /dataservice/device/dhcp/interface?deviceId=deviceId
Hardware                /dataservice/hardware/alarms?deviceId=deviceId
Interface               /dataservice/device/interface?deviceId=deviceId
                        /dataservice/device/interface/stats?deviceId=deviceId
                        /dataservice/device/interface/error_stats?deviceId=deviceId
IP                      /dataservice/device/ip/routetable?deviceId=deviceId
NTP                     /dataservice/device/ntp/associations?deviceId=deviceId
Reboot History          /dataservice/device/reboothistory?deviceId=deviceId
Software                /dataservice/device/software?deviceId=deviceId
System                  /dataservice/device/system/status?deviceId=deviceId
Tunnel                  /dataservice/device/tunnel/statistics?deviceId=deviceId

full_list : https://developer.cisco.com/docs/sdwan/device-realtime-monitoring/#realtime-monitoring-api-endpoints

"""

import requests
from a_get_login import authenticate
import json
import pprint

vmanage_ip = '192.168.71.80'
device_id = '100.255.34.1'
api_int_info = f'/dataservice/device/interface?deviceId={device_id}'
session = authenticate()

# === get interface info ===

def get_devices():
    
    url_device = f'https://{vmanage_ip}:443{api_int_info}'

    response = session.get(url=url_device,verify=False)
    if response.status_code == 200:
        print ("Get Devices Success")
        data = response.json()
        print(json.dumps(data['data'][0], indent=2))
        """
                {
        "vdevice-name": "100.255.34.1",
        "rx-errors": 0,
        "tx-kbps": 19,
        "if-admin-status": "if-state-up",
        "ipv6-tcp-adjust-mss": "0",
        "tx-pps": 12,
        "tx-errors": 0,
        "ifname": "GigabitEthernet0/0/0",
        "interface-type": "iana-iftype-ethernet-csmacd",
        "rx-pps": 13,
        "if-oper-status": "if-oper-state-ready",
        "ifindex": "1",
        "num-flaps": "5",
        "ipv4-tcp-adjust-mss": "0",
        "rx-packets": 20468086,
        "bia-address": "2c:4f:52:7a:b3:00",
        "vpn-id": "0",
        "vdevice-host-name": "IST-BR-1-R1",
        "ipv4-subnet-mask": "0.0.0.0",
        "mtu": "1500",
        "rx-drops": 0,
        "tx-drops": 0,
        "hwaddr": "2c:4f:52:7a:b3:00",
        "ip-address": "0.0.0.0",
        "speed-mbps": 1000,
        "auto-downstream-bandwidth": "N/A",
        "vdevice-dataKey": "100.255.34.1-0-GigabitEthernet0/0/0-0.0.0.0-2c:4f:52:7a:b3:00",
        "tx-octets": 125098191,
        "auto-upstream-bandwidth": "N/A",
        "tx-packets": 178194218,
        "rx-kbps": 18,
        "rx-octets": 3408232353,
        "lastupdated": 1716497405417
        }

        """
    else:
        print (f"Get Devices Failed : {response.content}")

get_devices()