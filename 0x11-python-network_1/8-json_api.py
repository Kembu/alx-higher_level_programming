#!/usr/bin/python3
"""Getting a request using requests package"""

import requests
from sys import argv as av

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        params = av[1]
    except IndexError:
        params = ""
    res = requests.post(url, {'q': params})
    header = res.headers['Content-type']
    if header == 'application/json':
        my_dict = res.json()
        if my_dict:
            print(f'[{my_dict["id"]}] {my_dict["name"]}')
        else:
            print('No result')
    else:
        print('Not a valid JSON')
