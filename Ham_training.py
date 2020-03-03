import requests
import json

url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/30/"

response = requests.get(url)
data = response.json()

# print(data)
streets = data['streets']
# print(streets[0])
# print(streets[3])

device = streets.get['device']
print(device)