#!/usr/bin/python3
"""Getting a request using requests package"""

import requests
from sys import argv as av

if __name__ == '__main__':
    data = {'email': av[2]}
    print(requests.post(av[1], data).text)
