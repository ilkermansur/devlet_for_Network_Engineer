
"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Create VRF ARGs===

tn_name = "tn_st01_name"
vrf_name = "vrf_st01_name"
vrf_alias = "vrf_st01_alias"
vrf_desc = "vrf_st01_desc"
url = "192.168.222.240"
username = "admin"
password = "Aa123456"

"""

import requests
import urllib3
import json
from Course_Notes.aci_scripts.a_aci_login import login

tn_name = "tn_st01_name"
vrf_name = "vrf_st01_name"
vrf_alias = "vrf_st01_alias"
vrf_desc = "vrf_st01_desc"
url = '192.168.222.240'
username = "admin"
password = "Aa123456"

################# SCRIPT #################

token =  login(url,username,password)
base_url = f"https://{url}/api"
pre_payload = {
  "fvTenant": {
    "attributes": {
      "dn": f"uni/tn-{tn_name}",
      "status": "modified"
    },
    "children": [
      {
        "fvCtx": {
          "attributes": {
            "dn": f"uni/tn-{tn_name}/ctx-{vrf_name}",
            "name": vrf_name,
            "nameAlias": vrf_alias,
            "descr": vrf_desc,
            "rn": f"ctx-{vrf_name}",
            "status": "created"
          },
          "children": []
        }
      }
    ]
  }
}

payload = json.dumps(pre_payload)
create_vrf_url = base_url + f"/node/mo/uni/tn-{tn_name}.json"

try:
    def create_vrf ():
        response = requests.post(url = create_vrf_url,
                                data = payload,
                                cookies={"APIC-Cookie":token},
                                verify=False)
        if response.status_code == 200:
            print (f"{vrf_name} is created")
        else:
            print (f"error is occurred : {response.status_code} {response}")
except Exception as e:
    print (f"error is occured : {e}")

create_vrf()
