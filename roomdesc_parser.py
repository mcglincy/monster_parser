#!/usr/bin/python3

import json
from roomdesc import *


filename = './datafiles/roomdesc.mon'
with open(filename, 'rb') as f:
  roomdescs = []
  # 752
  for i in range(0, 752):
    roomdesc = read_roomdesc(f)
    roomdesc["id"] = i
    roomdescs.append(roomdesc)
  print(json.dumps(roomdescs, indent = 2, sort_keys=False))



