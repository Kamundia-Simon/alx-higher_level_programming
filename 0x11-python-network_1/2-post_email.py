#!/usr/bin/python3
"""
sends a POST request to the passed URL with a given email
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        b = response.read()
        print(b.decode('utf-8'))
