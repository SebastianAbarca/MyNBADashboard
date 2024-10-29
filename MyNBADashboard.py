import streamlit as st
import requests
import json

base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/"
url_addition = "PlayerDataAdvancedPlayoffs/name/Kyrie Irving"


##sample GET request
# Make the GET request
print("making get request")
response = requests.get(base_url+url_addition)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response (if applicable) and print it
    data = response.json()
    print("Success Response:")
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")