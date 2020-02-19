#!/usr/bin/python3

import json
from roomdesc import *


filename = './datafiles/roomdesc.mon'
with open(filename, 'rb') as f:
  roomdescs = []
  record_index = 1  # 1-based
  # 752 records
  while has_more_data(f):
    roomdesc = read_roomdesc(f)
    roomdesc["id"] = record_index
    record_index = record_index + 1
    roomdescs.append(roomdesc)
  print(json.dumps(roomdescs, indent = 2, sort_keys=False))



