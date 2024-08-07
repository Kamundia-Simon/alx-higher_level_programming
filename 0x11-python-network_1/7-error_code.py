#!/usr/bin/python3
"""Script that sends a request to a given URL and displays the response body"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
