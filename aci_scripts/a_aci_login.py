"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur
"""

import json
import requests
import urllib3

try:

	def login(url, username, password):
        # define base URL
		base_url = f'https://{url}/api/'

        # create credentials structure
		name_pwd = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
		json_credentials = json.dumps(name_pwd)
        
        # log in to API
		login_url = base_url + 'aaaLogin.json'
        
        # disable warnings about SSL
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		response = requests.post(url=login_url, data=json_credentials, verify=False)
        
        # get token from login response structure
		data = response.json()
		token = data['imdata'][0]['aaaLogin']['attributes']['token']
		print ('Getting TOKEN Succesfully')
		return token

except Exception as e:

	#Print error code and explaination
	print (f'Error: {e}')