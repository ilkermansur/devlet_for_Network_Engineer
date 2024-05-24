"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== Tenant List ARGs ===
no arguments

"""

import requests
import urllib3
from Course_Notes.aci_scripts.a_aci_login import login

token = login(url='192.168.222.240',username='admin',password='Aa123456')

url = '192.168.222.240'
base_url = f'https://{url}/api/'


headers = {
	"Cookie": f"APIC-cookie={token}"
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

tenant_list = base_url + "node/class/fvTenant.json"
response = requests.get(tenant_list, headers=headers, verify=False)

tenants = response.json()['imdata']

for tenant in tenants:
    print(tenant['fvTenant']['attributes']['name'])

