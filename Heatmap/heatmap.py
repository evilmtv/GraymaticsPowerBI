# -*- coding: utf-8 -*-
"""
Heatmap generator from json and picture

Version: v1.0.0 (tested on Python 3.6.4)
Developed By: Lim Jun Hao
Company: Graymatics Inc
"""

import sys
from tkinter.filedialog import askopenfilename
import json
from heatmappy import Heatmapper
from PIL import Image

# Ensure script is run on python 3.5.2 and above
try:
    assert sys.version_info >= (3,5,2)
except AssertionError:
    print ('Please use Python 3.6 : https://www.python.org/downloads/ \n')
    raise

# Read original data
filename = askopenfilename()
with open(filename) as temp:
    newdata = temp.read()

data = json.loads(newdata)
coord_list = []
for key, value in data.items():
    coord_pair = (float(value.pop("x_coord", None)), float(value.pop("y_coord", None)))
    coord_list.append(coord_pair)

example_img_path = 'test.jpg'
example_img = Image.open(example_img_path)

heatmapper = Heatmapper()
heatmap = heatmapper.heatmap_on_img(coord_list, example_img)
heatmap.save('heatmapnottest.png')
