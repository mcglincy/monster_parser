from read import *

# ObjectRec = RECORD
#   ObjName   : ShortString;   { duplicate of name of object }
#   Kind      : INTEGER;       { what kind of object this is }
#   LineDesc  : INTEGER;       { liner desc of object Here }
#   Wear      : INTEGER;       { where object is equipped }
#   Weight    : INTEGER;       { move speed modifier }
#   Examine   : INTEGER;       { desc block for close inspection }
#   Worth     : INTEGER;       { how much it cost to make (in gold) }
#   NumExist  : INTEGER;       { number in existence }
#   Sticky    : BYTE_BOOL;       { can they ever get it? }
#   GetObjReq : INTEGER;       { object required to get this object }
#   GetFail   : INTEGER;       { fail-to-get description }
#   GetSuccess: INTEGER;       { successful picked up description }
#   UseObjReq : INTEGER;       { object require to use this object }
#   UseLocReq : INTEGER;       { place have to be to use this object }
#   UseFail   : INTEGER;       { fail-to-use description }
#   UseSuccess: INTEGER;       { successful use of object description }
#   Particle  : INTEGER;       { a,an,some, etc... "particle" is not }
#                              { be right, but hey, it's in the code }
#   Component : ARRAY [1..MaxComponent] OF INTEGER;
#                              { components of the particular object.}
#   Parms : ARRAY [1..MaxParm] of INTEGER;
#   D1: INTEGER;               { extra description # 1 }
#   D2: INTEGER;               { extra description # 2 }
#   Holdability : INTEGER;     { how easy to hold object (% to hold) }
#   Alignment   : INTEGER;
#   Extra2  : INTEGER;
# END;

# maxparm = 20;   { parms for object USEs }
MAX_PARM = 20

# maxcomponent = 7; { number of object components }
MAX_COMPONENT = 7

def read_object(f):
  obj = {}
  obj['obj_name'] = read_short_string(f)
  obj['kind'] = read_integer(f)
  obj['line_desc'] = read_integer(f)
  obj['wear'] = read_integer(f)
  obj['weight'] = read_integer(f)
  obj['examine'] = read_integer(f)
  obj['worth'] = read_integer(f)
  obj['num_exist'] = read_integer(f)
  obj['sticky'] = read_bytebool(f)
  obj['get_obj_req'] = read_integer(f)
  obj['get_fail'] = read_integer(f)
  obj['get_success'] = read_integer(f)
  obj['use_obj_req'] = read_integer(f)
  obj['use_loc_req'] = read_integer(f)
  obj['use_fail'] = read_integer(f)
  obj['use_success'] = read_integer(f)
  obj['particle'] = read_integer(f)
  obj['components'] = []
  for i in range(0, MAX_COMPONENT):
    component = read_integer(f)
    if component > 0:
      obj['components'].append(component)
  obj['parms'] = []
  for j in range(0, MAX_PARM):
    parm = read_integer(f)
    if parm > 0:
      obj['parms'].append(parm)
  obj['d1'] = read_integer(f)
  obj['d2'] = read_integer(f)
  obj['holdability'] = read_integer(f)
  obj['alignment'] = read_integer(f)
  obj['extra'] = read_integer(f)
  # TODO: there's one extra byte in the record???
  f.read(1)
  return obj