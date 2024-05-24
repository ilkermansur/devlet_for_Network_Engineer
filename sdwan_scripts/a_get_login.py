"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

=== login ARGs===
vmanage_ip = '192.168.71.80'
username = "admin"
password = "admin123"

"""
import requests
import json

# Disable warnings about SSL (optional)
requests.packages.urllib3.disable_warnings()

# Function to authenticate
def authenticate(vmanage_ip="192.168.71.80", username="admin", password="admin123"):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'j_username': username, 'j_password': password}
    session = requests.session()
    response = session.post(url=f'https://{vmanage_ip}/j_security_check',
                             headers=headers,
                             data=payload, 
                             verify=False)
    
    if response.status_code == 200:
        print("Authentication successful!")
        return session
    else:
        print("Authentication failed!")
        exit()


