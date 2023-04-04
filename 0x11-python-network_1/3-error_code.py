#!/usr/bin/python3
"""Handling of errors with urllib"""

from urllib.error import HTTPError
from urllib.request import urlopen
import sys

if __name__ == '__main__':
    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except HTTPError as error:
        print(f'Error code: {error.status}')
