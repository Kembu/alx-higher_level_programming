#!/usr/bin/python3
"""Getting a request using requests package"""

import requests
from sys import argv as av

if __name__ == '__main__':
    try:
        res = requests.get(av[1])
        error = res.raise_for_status()
        if not error:
            print(res.text)
    except requests.exceptions.HTTPError as error:
        if (res.status_code > 400):
            print(f'Error code: {res.status_code}')
