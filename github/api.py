
'''

Status:	live
Application ID:	ca68432c
This is the application ID, you should send with each API request.
Application Keys:
6ca30555688657bf67e50280191ef3f2
d4eb41a9211e032741f306df7b0b3bb7
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import optparse


def callPublicFlightAPI(options):
    url = 'https://api.schiphol.nl/public-flights/flights?includedelays=false&page=0&sort=%2BscheduleTime'

    headers = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': 'ca68432c',
	  'app_key': 'd4eb41a9211e032741f306df7b0b3bb7'
	}

    try:
        response = requests.request('GET', url, headers=headers)
    except requests.exceptions.ConnectionError as error:
        print(error)
        sys.exit()

    if response.status_code == 200:
        flightList = response.json()
        print('found {} flights.'.format(len(flightList['flights'])))
        for flight in flightList['flights']:
            print('Found flight with name: {} scheduled on: {} at {}'.format(
                flight['flightName'],
                flight['scheduleDate'],
                flight['scheduleTime']))
    else:
        print('''Oops something went wrong
Http response code: {}
{}'''.format(response.status_code,
             response.text))

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-i', '--app_id', dest='app_id',
                      help='App id used to call the API')
    parser.add_option('-k', '--app_key', dest='app_key',
                      help='App key used to call the API')

    (options, args) = parser.parse_args()
    if options.app_id is None:
        parser.error('Please provide an app id (-i, --app_id)')

    if options.app_key is None:
        parser.error('Please provide an app key (-key, --app_key)')

    callPublicFlightAPI(options)

response = requests()

