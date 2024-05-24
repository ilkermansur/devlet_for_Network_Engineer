"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Create Tenant ARGs===

tn_name = "tn_st_01_name"
tn_alias = "tn_st_01_alias"
tn_desc = "tn_st_01_desc"

"""

import requests
import urllib3
import json
from Course_Notes.aci_scripts.a_aci_login import login

tn_name = "tn_st01_name"
tn_alias = "tn_st01_alias"
tn_desc = "tn_st01_desc"

################# SCRIPT #################

url = "192.168.222.240"
token = login (url="192.168.222.240",username="admin",password="Aa123456")
base_url = f"https://{url}/api"

pre_payload = {
    "fvTenant":{
        "attributes":{
            "dn":f"uni/tn-{tn_name}",
            "name":f"{tn_name}",
            "nameAlias":f"{tn_alias}",
            "descr":f"{tn_desc}",
            "rn":f"tn-{tn_name}",
            "status":"created"},
            "children":[]
            }           
}

payload = json.dumps(pre_payload)
create_tenant_url = base_url+f"/node/mo/uni/tn-{tn_name}.json"

try:
    def create_tenant ():
        response = requests.post(url=create_tenant_url,
                                cookies={"APIC-Cookie":token},
                                data=payload,
                                verify=False)
        if response.status_code == 200 :
            print (f"Creating tenant {tn_name} succesfully")
            print (response)
        else:
            print (response)
except Exception as e:
    print (f"Error occurred {e}")

create_tenant()
