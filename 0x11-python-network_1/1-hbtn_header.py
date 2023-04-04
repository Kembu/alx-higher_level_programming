#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import sys
    from urllib.request import urlopen
    with urlopen(sys.argv[1]) as f:
        print(f.getheader('X-Request-Id'))
