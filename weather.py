from __future__ import division
import urllib3
import json

baseurl = 'http://api.openweathermap.org/data/2.5/weather'
consumer_key = '2bc3e79bb974a007818864813f53fd35'
http = urllib3.PoolManager()


def weather_finder(city='Nairobi'):
    r = http.request('GET', baseurl, fields={
                     'q': city, 'appid': consumer_key, 'units': 'metric'})
    return json.loads(r.data.decode('utf-8'))


def get_weather_details(cities):
    weather_details = {}
    for city in cities:
        temp_list = []
        response = weather_finder(city)
        temp_list.append(response['main']['temp'])
        temp_list.append(response['weather'][0]['description'])
        weather_details[city] = temp_list
    return weather_details

details = get_weather_details(['Nairobi', 'Kampala', 'London'])

print '{:10s} {:10s}  {:20s}'.format('City', 'Temperature', 'Description ')
print '=' * 40
for key in details:
    print '{:10s} {:10s}  {:20s}'.format(key,
                                         str(details[key][0]), details[key][1])
