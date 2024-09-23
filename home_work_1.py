import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

city = input('Введите город: ')
query = input('Что найти?(кафе, парки и т.д.): ')
page_size = input('Сколько объектов вывести?: ')

url = 'https://catalog.api.2gis.com/3.0/items'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/128.0.0.0 Safari/537.36',
           'Accept': '*/*'}

city_params = {
    'q': city,
    'key': os.getenv('2GIS_KEY')
}
city_response = requests.get(url, params=city_params, headers=headers).json()
city_id = city_response.get('result').get('items')[0].get('id')

params = {
    'q': query,
    'city_id': city_id,
    'page_size': page_size,
    'key': os.getenv('2GIS_KEY')
}

response = requests.get(url, params=params, headers=headers)

json_data = response.json()

for unit in json_data.get('result').get('items'):
    if unit.get("address_name") is not None:
        print(f'{unit.get("name")} - {unit.get("address_name")}')
    else:
        print(unit.get("name"))
