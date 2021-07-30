from pprint import pprint
import requests

url = 'https://api.schiphol.nl/public-flights/flights'
params = {'accept': 'application/json',
          'resourceversion': 'v4',
          'app_id': 'ca68432c',
          'app_key': 'd4eb41a9211e032741f306df7b0b3bb7'
}

response = requests.get(url, params=params)
pprint(response.json())

with open('task_2.json', 'w') as f:
    f.write(response.text)