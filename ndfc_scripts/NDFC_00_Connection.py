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
#
#print (jwttoken)

# Use token in headers
headers = {
    'Authorization' : 'Bearer '+ jwttoken, 
           'Content-Type': 'application/json'
           }

############################################################# EXMPLE REQUEST #############################################################
    # 'Network information'


""" fabric_name = 'Vakifbank_Lab_Fabric'
try:
    network_information = requests.get(url=url+f'/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/v2/fabrics/{fabric_name}/netinfo',
                                    headers=headers,
                                    json=payload,
                                    verify=False)
    
    if network_information.status_code == 200:
        response_log = network_information.json()
        #print (response_log)
    else:
        error_log = network_information.json()
        print (error_log)

except Exception as e:
    print (e.json())
 """
############################################################# EXMPLE REQUEST #############################################################
    # 'list Network'

""" fabric_name = 'Vakifbank_Lab_Fabric'
try:
    network_information = requests.get(url=url+f'/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/v2/fabrics/{fabric_name}/networks',
                                    headers=headers,
                                    json=payload,
                                    verify=False)
    
    if network_information.status_code == 200:
        response_log = network_information.json()
        print (response_log)
    else:
        error_log = network_information.json()
        print (error_log)

except Exception as e:
    print (e.json()) """