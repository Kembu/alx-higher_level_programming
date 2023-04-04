#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    """Opening a url with a context manager"""
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as f:
        html = f.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')
