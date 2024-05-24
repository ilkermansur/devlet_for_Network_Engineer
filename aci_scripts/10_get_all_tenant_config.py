"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Get Specific Class ARGs===
url = '192.168.222.240'

= Some_Class_Name =
Tenant: fvTenant
Application Profile: fvAp
Application End Point Group(EPG): fvAEPg
Bridge domain: fvBD
Subnet: fvSubnet

"""
import requests
from Course_Notes.aci_scripts.a_aci_login import login
import json

url = "192.168.222.240"
username = "admin"
password = "Aa123456"
cookies = login(url=url, username = username, password = password)

tenant_name = "tn_st01_name"

headers = {
    "Content-Type" : "application/json",
    "connection" : "keep-alive"
}
try:
    def get_all_tenant_config (
            url = f"https://{url}//api/mo/uni/tn-{tenant_name}.json?rsp-subtree=children",
            cookies = cookies):
        response = requests.get(url=url,
                                cookies= {"APIC-Cookie":cookies},
                                headers= headers,
                                verify= False)
        print (response.status_code)
        json_data = response.json()

        print (json.dumps(json_data,indent=4))

except Exception as e:
    print (f"error occured : {e}")

get_all_tenant_config()