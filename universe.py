from read import *

# Universe = RECORD
#   Name    :ShortString;  (* Name of the universe *)
#   Desc    :String;       (* A description of the universe *)
#   UnivSpecificOps :ARRAY [1..MaxUnivSpecificOps] of String;
#   Daemon              :ShortString;
#   Random              :ShortString;
# END;

# MaxUnivSpecificOps = 5; (* How many extra ops per universe *)
MAX_UNIV_SPECIFIC_OPS = 5

def read_universe(f):
  univ = {}
  univ['name'] = read_short_string(f)
  univ['desc'] = read_string(f)
  univ['univ_specific_ops'] = []
  for i in range(0, MAX_UNIV_SPECIFIC_OPS):
    op = read_string(f)
    if len(op) > 0:
      univ['univ_specific_ops'].append(op)
  univ['daemon'] = read_short_string(f)
  univ['random'] = read_short_string(f)
  return univ