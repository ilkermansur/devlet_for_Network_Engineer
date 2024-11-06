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
payload = {
  "userName": username,
  "userPasswd": password,
  "domain": domain
}
# Use verify=False if you are sure the target system is the system you expect and it has a self-signed certificate.

response = requests.post(url='https://192.168.221.130/login', json=payload, verify=False)

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
del_network = 'MyNetwork_30040'

delurl = f'https://{host}/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/fabrics/{fabric_name}/networks/{del_network}'

response_del_network = requests.delete(url=delurl,
                                        headers=headers,
                                        verify=False
                                       )

if response_del_network.status_code == 200:
    try:
        response_log = response_del_network.json()
    except json.decoder.JSONDecodeError:
         print ('Islem Basarili fakat bos cevap donuyor')

else: 
    response_log = response_del_network.json()
    print (response_log)




