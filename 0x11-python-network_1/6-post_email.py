#!/usr/bin/python3
"""sends a POST request to the passed URL with the passed email as a parameter
   displays the body of the response"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    response = requests.post(url, data=payload)
    print(response.text)
