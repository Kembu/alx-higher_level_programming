#!/usr/bin/python3
"""Getting a request using requests package"""

import requests
from sys import argv as av

if __name__ == '__main__':
    print(requests.get(av[1]).headers.get('X-Request-Id'))
