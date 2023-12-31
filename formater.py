from json import dumps

d = {'status': 'success', 'msg': None, 'data': {'text': 'Very poor', 'alert': 'Very poor air quality index in this location. It may cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.', 'color': 'red', 'value': 351, 'index': 5, 'updated': 'Sun Dec 31 15:05:33 +0000 2023', 'temp': '13', 'content': None, 'country': 'India', 'clouds': 'description = mist, image = https://airpollutionapi.com/images/icons/50n.png', 'coordinates': {'latitude': 28.704059, 'longitude': 77.10249}, 'source': {'name': 'SAFAR - India, Pusa Delhi', 'coordinates': {'latitude': 28.6376724, 'longitude': 77.1571443}}, 'accuracy': '9.11 Km', 'dominating': 'PM2.5', 'aqiParams': [{'name': 'O3', 'value': 'AQI 63', 'aqi': 63, 'color': '#bbcf4c;', 'text': 'Satisfactory', 'updated': 'Sun Dec 31 15:05:33 +0000 2023'}, {'name': 'PM2.5', 'value': 'AQI 351', 'aqi': 351, 'color': '#A52A2A;', 'text': 'Severe', 'updated': 'Sun Dec 31 15:05:33 +0000 2023'}, {'name': 'PM10', 'value': 'AQI 229', 'aqi': 229, 'color': '#FFCF00;', 'text': 'Moderate', 'updated': 'Sun Dec 31 15:05:33 +0000 2023'}, {'name': 'Humidity', 'value': '82.0 %', 'aqi': None, 'color': None, 'text': None, 'updated': None}, {'name': 'Barometric Pressure', 'value': '1018.0 hPa', 'aqi': None, 'color': None, 'text': None, 'updated': None}, {'name': 'Wind Speed', 'value': ' 4.61 m/s', 'aqi': None, 'color': None, 'text': None, 'updated': None}, {'name': 'Wind Direction', 'value': '30.0 degrees', 'aqi': None, 'color': None, 'text': None, 'updated': None}]}}

print(dumps(d['data'], indent=4))

