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
vrf_name = 'VRF_3041'
vrf_id = 3041
vlan_id = 3041
#####################################################################################################################

payload = {
  "fabric": fabric_name,
  "vrfName": vrf_name,
  "vrfTemplate": "Default_VRF_Universal",
  "vrfExtensionTemplate": "Default_VRF_Extension_Universal",
  "vrfTemplateConfig": f"""
  {{
    "vrfVlanName":{vrf_name},
    "vrfIntfDescription":{vrf_name},
    "vrfDescription":{vrf_name},
    "mtu":"9216",
    "tag":"12345",
    "vrfRouteMap":"FABRIC-RMAP-REDIST-SUBNET",
    "maxBgpPaths":"1",
    "maxIbgpPaths":"2",
    "ipv6LinkLocalFlag":"true",
    "trmEnabled":"false",
    "isRPAbsent":false,
    "isRPExternal":false,
    "rpAddress":"",
    "loopbackNumber":"",
    "L3VniMcastGroup":"",
    "multicastGroup":"",
    "trmBGWMSiteEnabled":false,
    "advertiseHostRouteFlag":"false",
    "advertiseDefaultRouteFlag":"true",
    "configureStaticDefaultRouteFlag":"true",
    "bgpPassword":"",
    "bgpPasswordKeyType":"3",
    "ENABLE_NETFLOW":"false",
    "NETFLOW_MONITOR":"",
    "disableRtAuto":"false",
    "routeTargetImport":"",
    "routeTargetExport":"",
    "routeTargetImportEvpn":"",
    "routeTargetExportEvpn":"",
    "routeTargetImportMvpn":"",
    "routeTargetExportMvpn":"",
    "vrfName":{vrf_name},
    "vrfVlanId":{vlan_id},
    "vrfSegmentId":{vlan_id},
    "nveId":"1",
    "asn":""
    }}""",
  "vrfId": vrf_id
}


add_vrf_url = f'https://{host}/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/fabrics/{fabric_name}/vrfs'



response_add_vrf = requests.post(url=add_vrf_url,
                                        headers=headers,
                                        verify=False,
                                        json=payload
                                       )

if response_add_vrf.status_code == 200:
    try:
        response_log = response_add_vrf.json()
        print (response_log)
    except json.decoder.JSONDecodeError:
         print ('Islem Basarili fakat bos cevap donuyor')

else: 
    response_log = response_add_vrf.json()
    print (response_log)




