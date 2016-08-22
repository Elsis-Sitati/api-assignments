import urllib3, json


def weather_finder(city = 'Nairobi'):
    baseurl = 'http://api.openweathermap.org/data/2.5/weather'
    consumer_key = '2bc3e79bb974a007818864813f53fd35'
    http = urllib3.PoolManager()
    r = http.request('GET', baseurl,fields = {'q': city,'appid': consumer_key,'units': 'metrics'})
    return json.loads(r.data.decode('utf-8'))
    

def get_weather_details(cities):
    weather_details = {}
    for city in cities:
        response = weather_finder(city)
        temp = {}
        temp['weather'] = response['weather'][0]['description'] 
         #contains temp, pressure, humidity, temp_min, temp-max
        temp.update(response['main'])
        #print temp 
        weather_details[city] = temp
    return weather_details

print(get_weather_details(['Nairobi','Kampala','London']))