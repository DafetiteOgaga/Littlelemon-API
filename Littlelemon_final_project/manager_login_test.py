#!/usr/bin/env python3

import requests

# Define the URL
url = 'http://127.0.0.1:8000/auth/token/login/'

# Define the payload (username and password)
payload = {
    'username': 'dickson',
    'password': 'dick1234'
}

# Make the POST request
response = requests.post(url, data=payload)

# Check the response status code
if response.status_code == 200:
    # Print the response content (token)
    print("Token:", response.json()['auth_token'])
else:
    # Print the error message
    print("Error:", response.text)
