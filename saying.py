from read import *

# Saying = RECORD
#   KeyWord : String;    (* What word will make the random say the saying *)
#   Saying : String;     (* What the random says in response to the keyword *)
# END;

def read_saying(f):
  s = {}
  s['keyword'] = read_string(f)
  s['saying'] = read_string(f)
  return s    