# -*- coding: utf-8 -*-
"""
Make invalid output into valid output. MAGIC! http://www.reactiongifs.com/r/mgc.gif

Version: v1.3.0 (tested on Python 3.6.4 & 3.5.2)
Developed By: Lim Jun Hao
Company: Graymatics Inc
"""

import json
import os
import sys
from collections import OrderedDict
from tkinter.filedialog import askopenfilename

# Ensure script is run on python 3.5.2 and above
try:
    assert sys.version_info >= (3,5,2)
except AssertionError:
    print ('Please use Python 3.6 : https://www.python.org/downloads/ \n')
    raise

# Read original data
filename = askopenfilename()
f = open(filename,'r')
lines = f.readlines()  # read old content
f.close()

# Add square brackets to start and end of json file
filedata = open('jsoncleaner_temp.json','w')
filedata.write("[")  # write new content at the beginning
for line in lines: # write old content after new
    filedata.write(line)
filedata.write("]\n")  # write new content at the end
filedata.close()

# Add missing comma in between keys
with open('jsoncleaner_temp.json') as temp:
    newdata = temp.read().replace('}\n{', '},\n{')  # Replace the target string

data = json.loads(newdata)

# Prepare variables
count = 0
newdata = OrderedDict()
first_time_flag = True

for dataset in data:
    # Clean unnecessary data
    dataset.pop("_id", None)
    dataset.pop("scene_id", None)
    dataset.pop("user_id", None)
    dataset.pop("camera_id", None)
    dataset.pop("camera_name", None)
    dataset.pop("type", None)
    dataset.pop("message", None)
    dataset.pop("frame", None)
    dataset.pop("status", None)
    dataset.pop("end_time", None)
    dataset.pop("start_time", None)
    dataset['result']['PEOPLE_TRACKING'].pop("count", None)
    dataset.pop("__v", None)

    # Save current timestamp
    if (first_time_flag is True):
        first_time_flag = False
        first_timestamp = float(dataset.pop("timestamp", None))
        current_timestamp = 0
    else:
        current_timestamp = round((float(dataset.pop("timestamp", None)) - first_timestamp), 2)
    total = dataset['result']['PEOPLE_TRACKING'].pop("total", None)

    # Arrange data into a useful order
    for key, value in dataset['result']['PEOPLE_TRACKING']['person'].items():
        newdata[str(count)] = OrderedDict() # Create key
        newdata[str(count)]['timestamp'] = str(current_timestamp)
        newdata[str(count)]['total_passed'] = str(total)
        newdata[str(count)]['person_id'] = str(key)
        newdata[str(count)]['x_coord'] = str((value[0]+value[2])/2)
        newdata[str(count)]['y_coord'] = str((value[1]+value[3])/2)
        newdata[str(count)]['count_on_screen'] = str(len(dataset['result']['PEOPLE_TRACKING']['person'].keys()))
        count += 1

print(newdata)

print ("Cleaning up files...")
os.remove("jsoncleaner_temp.json")

print ("Writing json file to cleaned_output.json...")
with open('cleaned_output.json', 'w') as outfile:
    json.dump(newdata, outfile, indent=4, sort_keys=False)

print ("Done!")
