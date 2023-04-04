#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import sys
    from urllib import request, parse
    kv = {'email': sys.argv[2]}
    data = parse.urlencode(kv).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
