#!/usr/bin/python3
"""Getting  a request using requests package"""

import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status').text
    print('Body response:')
    print(f'\t- type: {type(response)}')
    print(f'\t- content: {response}')
