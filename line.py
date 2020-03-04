from read import *

# LineRec = RECORD
#   Line : String;   (* The text of a line *)
# END;

def read_line(f):
  line = {}
  line['line'] = read_string(f)
  return line