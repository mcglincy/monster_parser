
import json
from object import *


def parse_file(filename, reader_fn):
  with open(filename, 'rb') as f:
    objects = []
    record_index = 1  # 1-based
    while has_more_data(f):  
      obj = reader_fn(f)
      obj["id"] = record_index
      record_index = record_index + 1
      objects.append(obj)
  print(json.dumps(objects, indent = 2, sort_keys=False))
  #return objects
