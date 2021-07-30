'''

Status:	live
Application ID:	ca68432c
This is the application ID, you should send with each API request.
Application Keys:
6ca30555688657bf67e50280191ef3f2
d4eb41a9211e032741f306df7b0b3bb7
'''

import requests
import sys
import optparse

my_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
              'accept': 'application/json',
              'resourceversion': 'v4',
              'app_id': 'ca68432c',
              'app_key': 'd4eb41a9211e032741f306df7b0b3bb7'
}

#params = {}
url = 'https://api.schiphol.nl/public-flights/flights'
#url = 'https://api.schiphol.nl/public-flights/flights?includedelays=false&page=0&sort=%2BscheduleTime'

response = requests.get(url, headers=my_headers)
print(response.text)