"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Create Application Profile ARGs===

tn_name = "tn_st01_name"
bd_name = "bd_st01_name"
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
app_name = "app_st01_name"
app_alias = "app_st01_alias"
app_desc = "app_st01_desc"
url = '192.168.222.240'
username = "admin"
password = "Aa123456"

################# SCRIPT #################

token =  login(url,username,password)
base_url = f"https://{url}/api"

pre_payload = {
  "fvAp": {
    "attributes": {
      "dn": f"uni/tn-{tn_name}/ap-{app_name}",
      "name": app_name,
      "nameAlias": app_alias,
      "descr": app_desc,
      "rn": f"ap-{app_name}",
      "status": "created"
    },
    "children": []
  }
}
  
payload = json.dumps(pre_payload)
create_app_url = base_url + f"/node/mo/uni/tn-{tn_name}/ap-{app_name}.json"

try:
    def create_app_profile ():
        response = requests.post(url = create_app_url,
                                data = payload,
                                cookies={"APIC-Cookie":token},
                                verify=False)
        if response.status_code == 200:
            print (f"{app_name} is created")
        else:
            print (f"error is occurred : {response.status_code} {response}")
except Exception as e:
    print (f"error is occured : {e}")

create_app_profile()