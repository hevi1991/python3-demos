#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' info, todo '

from PIL import Image

import os

im = Image.open('sample.jpg')

w, h = im.size

im.thumbnail((1024, 768))

filename = os.path.splitext(im.filename)[0]

im.save(filename + '-thumbnail.jpg', 'jpeg')