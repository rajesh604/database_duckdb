# importing required libraries
import requests
import json

# Define the URL
url = 'http://127.0.0.1:80/query'

# Load the JSON file
with open('example.json', 'r') as f:
    payload = json.load(f)

# Send the request to the API by using the POST method
response = requests.post(url, json=payload)

# Print the response
print(json.loads(response.text))