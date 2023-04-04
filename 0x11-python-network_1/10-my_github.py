#!/usr/bin/python3
"""Getting a request using requests package"""

import requests
from sys import argv as av
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    try:
        user = av[1]
        pswd = av[2]
    except IndexError:
        print('Please enter a username and password')
        exit()
    auth = HTTPBasicAuth(user, pswd)

    auth = (user, pswd)

    res = requests.get(url, auth=auth)
    print(res.json().get('id'))
