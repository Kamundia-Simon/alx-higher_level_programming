#!/usr/bin/python3
"""Script that sends a request to the URL & displays the body"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            bd = res.read()
            print(bd.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
