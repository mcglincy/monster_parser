#!/usr/bin/python3

import json
from desc import *


filename = './datafiles/desc.mon'
with open(filename, 'rb') as f:
  descs = []
  record_index = 1  # 1-based
  # 1260 records
  while has_more_data(f):  
    desc = read_desc(f)
    desc["id"] = record_index
    record_index = record_index + 1
    descs.append(desc)
  print(json.dumps(descs, indent = 2, sort_keys=False))



