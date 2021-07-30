import requests
import json

USER = 'valentinagal'
URL = f'https://api.github.com/users/{USER}/repos'

req = requests.get(URL)
print(req.status_code)

json_data = req.json()
repos = [d['name'] for d in json_data]
print(repos)

with open('user_repos.json', 'w') as f:
    json.dump(json_data, f)