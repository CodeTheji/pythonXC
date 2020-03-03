import citylist
import requests
data = citylist.citylist


user_city = input("Please enter city name : ")
user_country = input("Please enter country name : ")

def fetch_id(user_city, user_country, data):
    city_id = ""

    for city in data:
        if city["name"] == user_city and city["country"] == user_country:
            city_id = city["id"]
            print(city["name"], city["country"], city["id"], "\n\n\n\n\n")
    
    return city_id

id = fetch_id(user_city, user_country, data)
print(id)
api_key = "336b102582e7d317c464efd5e6ac86aa"
url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"

r = requests.get(url)
# print(r.json())
file_name = "weather_data.py"

file = open(file_name, "w")
print(r.json(), file= file)
print(r.json())
