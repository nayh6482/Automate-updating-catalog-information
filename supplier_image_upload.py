#!/usr/bin/env python3
import requests,os

url = "http://localhost/upload/"
for image in os.listdir("supplier-data/images"):
    if "jpeg" in image:
        with open(image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
