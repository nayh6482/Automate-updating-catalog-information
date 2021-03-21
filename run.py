#!/usr/bin/env python3

import os
import requests, json

url = "http://localhost/fruits/"
path = "supplier-data/descriptions/"

for file in os.listdir(path):
    if file.endswith("txt"):
        with open(path + file, "r") as f:
            content = f.read()
            fruit_value_list = content.splitlines()
            fruit_name = fruit_value_list[0].strip()
            fruit_weight = int(fruit_value_list[1].strip().split()[0])
            fruit_description = fruit_value_list[2].strip()
            fruit_dict = {
                "name": fruit_name,
                "weight": fruit_weight,
                "description": fruit_description,
                "image_name": os.path.splitext(file)[0] + ".jpeg"
            }
            r = requests.post(url, json=fruit_dict)
            r.raise_for_status()
            print(r.request.url)
            print(r.status_code)
