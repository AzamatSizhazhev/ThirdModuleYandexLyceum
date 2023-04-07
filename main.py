import requests

list_of_cities = input().split(', ')
positions = dict()
for city in list_of_cities:
    geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json'
    response = requests.get(geocoder_request)
    json_response = response.json()
    positions[city] = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']['lowerCorner'].split()[-1]
print(min(positions, key=lambda unit: float(positions[unit])))
