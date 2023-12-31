from decouple import config
import requests

request_str = "http://api.airpollutionapi.com/1.0/aqi?lat=28.7040590&lon=77.10249&APPID={}".format(config('API_KEY'))
response = requests.get(request_str)

print(response.json()["data"])
