from read import *

# DescREC = RECORD
#   Lines: ARRAY [1..DescMax] of String; (* Lines in a block *)
#   DescLen: INTEGER;  { number of lines in this block }
# END;

# descmax = 10;   { lines per description block }
DESC_MAX = 10

def read_desc(f):
  """Should be ??? bytes.

  82 bytes per string * 10 = 820, +4 for INTEGER = 824.
  """
  desc = {}
  desc["lines"] = []
  for i in range(0, DESC_MAX):
    line = read_string(f)
    desc["lines"].append(line)
  desc_len = read_integer(f)
  desc["desc_len"] = desc_len
  desc["lines"] = desc["lines"][0:desc_len]
  return desc
