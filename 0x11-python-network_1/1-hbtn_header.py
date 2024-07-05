#!/usr/bin/python3
"""Script that sends a request to the URL & displays the value

of the X-Request-Id variable found in the header"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as resp:
        request = resp.getheader('X-Request-Id')
        print(request)
