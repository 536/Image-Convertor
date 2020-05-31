# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: png2ico.py
# Author: https://github.com/536
# Create Time: 2020-05-29 22:27
import os

import PythonMagick


def png2ico(file, size='32x32'):
    _file, ext = os.path.splitext(file)
    # if ext == '.png':
    img = PythonMagick.Image(file)
    img.sample(size)
    img.write(_file + '.ico')
