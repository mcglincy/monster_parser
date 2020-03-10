from read import *

# Exit =  RECORD
#   ToLoc   : INTEGER;      { Room this exit goes to }
#   Kind    : INTEGER;      { What kind of exit is this }
#   Slot    : INTEGER;      { Which direction does it come out in }
#   ExitDesc,               { one liner description of exit  }
#   DoorEffect,             { what happens when going through a door!! }
#   Fail,                   { description if can't go thru   }
#   Success,                { desc while going thru exit     }
#   Goin,                   { what others see when you go into the exit }
#   ComeOut : INTEGER;      { what others see when you come out of the exit }
#   Hidden  : INTEGER;      { if exit's hidden...block #}
#   ObjReq  : INTEGER;      { object required to pass this exit }
#   Alias   : VeryShortString; { alias for the exit dir, a keyword }
#   ReqVerb : BYTE_BOOL;      { require alias as a verb to work }
#   ReqAlias: BYTE_BOOL;      { require alias only (no direction) to }
#                           { pass through the exit }
#   AutoLook: BYTE_BOOL;      { do a look when user comes out of exit }
# END;

def read_exit(f):
  exit = {}
  exit["to_loc"] = read_integer(f)
  exit["kind"] = read_integer(f)
  exit["slot"] = read_integer(f)
  exit["exit_desc"] = read_integer(f)
  exit["door_effect"] = read_integer(f)
  exit["fail"] = read_integer(f)
  exit["success"] = read_integer(f)
  exit["go_in"] = read_integer(f)
  exit["come_out"] = read_integer(f)
  exit["hidden"] = read_integer(f)
  exit["obj_req"] = read_integer(f)
  exit["alias"] = read_very_short_string(f)
  exit["req_verb"] = read_bytebool(f)
  exit["req_alias"] = read_bytebool(f)
  exit["auto_look"] = read_bytebool(f)
  return exit
