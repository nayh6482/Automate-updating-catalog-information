#!/usr/bin/env python3

import os
from PIL import Image

size = (600, 400)
path = "supplier-data/images/"

for infile in os.listdir(path):
    if "tiff" in infile:
        outfile = path + os.path.splitext(infile)[0] + ".jpeg"
        if infile != outfile:
            Image.open(path + infile).convert("RGB").resize(size).save(outfile,"JPEG")
