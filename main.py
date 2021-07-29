from pprint import pprint
import requests
url = 'https://www.google.ru'

response = requests.get(url)
print()

response.status_code
response.ok
response.headers
response.content



response.text