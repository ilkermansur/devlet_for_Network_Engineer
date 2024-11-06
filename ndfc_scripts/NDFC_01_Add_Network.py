"""
Script for NDFC (Nexus Dashboard Fabric Controller)
reference : https://developer.cisco.com/docs/nexus-dashboard-fabric-controller/latest/#!api-reference-lan

"""


import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from pprint import pprint
import json

# Give parameters below

username = 'admin'
password = 'Aa123456'
host = '192.168.221.130'
domain = 'local'

#####################################################################################################################

url = f'https://{host}'

payload = {
  "userName": username,
  "userPasswd": password,
  "domain": domain
}

# Use verify=False if you are sure the target system is the system you expect and it has a self-signed certificate.

response = requests.post(url=url+'/login', json=payload, verify=False)

if response.status_code == 200 :
    print ('Connection is ok!')
else:
    print ('Connection error is occured :' + response.status_code)

# The default token duration is 20 minutes, but can be changed in the Nexus Dashboard GUI by navigating to 
# Admin Console > Administrative > Security and updating the Session Timeout field:

jwttoken = response.json()['jwttoken']

# Use token in headers
headers = {
    'Authorization' : 'Bearer '+ jwttoken, 
           'Content-Type': 'application/json'
           }

#####################################################################################################################
fabric_name = 'DC-1'
network_name = "MyNetwork_30040"
vrfName = "Net_Vlan_200_L3"
networkId = 30040
primaryNetworkId = 30040
vlan_Id = "1010"

#####################################################################################################################

payload = {
"fabric": fabric_name,
"networkName": network_name,
"displayName": network_name,
"networkId": networkId,
"networkTemplate": "Default_Network_Universal",
"networkExtensionTemplate": "Default_Network_Extension_Universal",
"networkTemplateConfig" : f"""
{{
    "gatewayIpAddress": "10.10.10.1/24",
    "gatewayIpV6Address": "",
    "vlanName": "",
    "intfDescription": "",
    "mtu": "",
    "secondaryGW1": "",
    "secondaryGW2": "",
    "secondaryGW3": "",
    "secondaryGW4": "",
    "type": "",
    "dhcpServerAddr1": "",
    "vrfDhcp": "",
    "dhcpServerAddr2": "",
    "vrfDhcp2": "",
    "dhcpServerAddr3": "",
    "vrfDhcp3": "",
    "suppressArp": "",
    "enableIR": "false",
    "mcastGroup": "239.1.1.2",
    "dhcpServers": "",
    "loopbackId": "",
    "tag": "12345",
    "trmEnabled": "",
    "rtBothAuto": "false",
    "ENABLE_NETFLOW": "false",
    "SVI_NETFLOW_MONITOR": "",
    "VLAN_NETFLOW_MONITOR": "",
    "enableL3OnBorder": "false",
    "vlanId": {vlan_Id},
    "segmentId": {networkId},
    "vrfName": "{vrfName}",
    "networkName": "{network_name}",
    "nveId": "1",
    "isLayer2Only": false
}}
""",
"vrf": vrfName,
"primaryNetworkId": primaryNetworkId,
"type": "Normal"
}


response_add_network = requests.post(url=url + f'/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/fabrics/{fabric_name}/networks',
                                        headers=headers,
                                        verify=False,
                                        json=payload)


if response_add_network.status_code == 200:
    response_log = response_add_network.json()
    print (response_log)
else: 
    response_log = response_add_network.json()
    print (response_log)