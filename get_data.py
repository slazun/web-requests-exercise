import json
import requests
print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products/2.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)