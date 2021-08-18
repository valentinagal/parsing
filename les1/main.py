
'''
from pprint import pprint
import requests
url = 'https://google.ru'
response = requests.get(url)
print()

response.status_code
#if response.status_code == 200:
#   pass
#else:
#    break
# if response.ok: еще один способ, будет работать, если ответ до 299

response.ok

response.headers

response.text

response.content

# pprint(dict(response.headers))
'''


# API

