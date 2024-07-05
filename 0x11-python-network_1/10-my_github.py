#!/usr/bin/python3
"""script that takes your GitHub credentials and displays id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    aut = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", aut=aut)
    print(res.json().get("id"))
