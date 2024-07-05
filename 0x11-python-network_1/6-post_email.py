#!/usr/bin/python3
""" Script that sends a POST request to the passed URL with the email"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    res = requests.post(url, data=data)

    print(res.text)
