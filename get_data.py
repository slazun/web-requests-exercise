import json
import requests
print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products.json"
response = requests.get(request_url)
#print(response.status_code)
#print(response.text)
response_data = json.loads(response.text)
print(type(response_data))
print(response_data)
#print(response_data['name'])

#for product in response_data:
#print(str(product['name']) + str(product['id'])

#for product in response_data:
    #print(product)

for product in response_data:
    print(str(product['name']) + " " + str(product['id']))
