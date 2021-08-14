import requests
import json

USER = 'maikelvdb'
URL = f'https://api.github.com/users/{USER}/repos'


r = requests.get(URL)
print(r.status_code)

data = r.json()
repos = [d['name'] for d in data]
print(repos)

with open('maikel_repos.json', 'w') as f:
    json.dump(data, f)
