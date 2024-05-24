"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Static Bindings ARGs===

tn_name = "tn_st01_name"
epg_name = "epg_st01_name"
app_name = "app_st01_name"
vlan_id = "200"
pod_id = "1"
node_id = "101"
port_id = "eth1/5"
url = '192.168.222.240'
username = "admin"
password = "Aa123456"
"""

import requests
import urllib3
import json
from Course_Notes.aci_scripts.a_aci_login import login

tn_name = "tn_st01_name"
epg_name = "epg_st01_name"
app_name = "app_st01_name"
vlan_id = "200"
pod_id = "1"
node_id = "101"
port_id = "eth1/5"
url = '192.168.222.240'
username = "admin"
password = "Aa123456"

################# SCRIPT #################

token =  login(url,username,password)
base_url = f"https://{url}/api"

pre_payload = {
  "fvRsPathAtt": {
    "attributes": {
      "dn": f"uni/tn-{tn_name}/ap-{app_name}/epg-{epg_name}/rspathAtt-[topology/pod-{pod_id}/paths-{node_id}/pathep-[{port_id}]]",
      "encap": f"vlan-{vlan_id}",
      "tDn": f"topology/pod-{pod_id}/paths-{node_id}/pathep-[{port_id}]",
      "rn": f"rspathAtt-[topology/pod-{pod_id}/paths-{node_id}/pathep-[{port_id}]]",
      "status": "created"
    },
    "children": []
  }
}
  
payload = json.dumps(pre_payload)

create_epg_url = base_url + f"/node/mo/uni/tn-{tn_name}/ap-{app_name}/epg-{epg_name}/rspathAtt-[topology/pod-{pod_id}/paths-{node_id}/pathep-[{port_id}]].json"

try:
    def static_binding ():
        response = requests.post(url = create_epg_url,
                                data = payload,
                                cookies={"APIC-Cookie":token},
                                verify=False)
        if response.status_code == 200:
            print (f"VLAN {vlan_id} is bind to {epg_name} - pod {pod_id} - node {node_id} - port {port_id} ")
        else:
            print (f"error is occurred : {response.status_code} {response}")
except Exception as e:
    print (f"error is occured : {e}")

static_binding()