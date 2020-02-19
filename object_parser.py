#!/usr/bin/python3

import json
from object import *


filename = './datafiles/objects.mon'
with open(filename, 'rb') as f:
  objects = []
  record_index = 1  # 1-based
  #for i in range(0, 3):
  while has_more_data(f):  
    obj = read_object(f)
    obj["id"] = record_index
    record_index = record_index + 1
    objects.append(obj)
  print(json.dumps(objects, indent = 2, sort_keys=False))



