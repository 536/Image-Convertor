# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: convertor.py
# Author: https://github.com/536
# Create Time: 2020-05-31 23:15
import os
from collections import OrderedDict

import PythonMagick

__all__ = [
    'convertor_dict'
]


def _convertor(file, size='32x32', input='png', output='ico'):
    _file, ext = os.path.splitext(file)
    img = PythonMagick.Image(file)
    img.sample(size)
    img.write(_file + '.' + output)


convertor_dict = OrderedDict()
convertor_dict['png2ico'] = lambda file, size: _convertor(file, size, 'png', 'ico')
convertor_dict['svg2ico'] = lambda file, size: _convertor(file, size, 'svg', 'ico')
convertor_dict['svg2png'] = lambda file, size: _convertor(file, size, 'svg', 'png')
