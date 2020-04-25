from people import *
from read import *

# Room = RECORD
#   People  :ARRAY [1..MaxPeople] of PeopleRec; { people in the room }
#   Objs  :ARRAY [1..MaxObjs] of INTEGER; { refs to object file }
#   ObjHide :ARRAY [1..MaxObjs] of INTEGER; { how much an object is hidden }
#   GoldHere  :INTEGER; { gold in the room }
#   ExitBlocked :ARRAY [1..MaxExit] OF INTEGER;
#   Extra1      : INTEGER;
# END;

# maxpeople = 10;   { max people allowed in a room }
MAX_PEOPLE = 10
# maxobjs = 15;   { max objects allow on floor in a room }
MAX_OBJS = 15
# maxexit = 6;    { 6 exits from each loc: NSEWUD }
MAX_EXIT = 6

def read_room(f):
  room = {}
  ppl = []
  for i in range(0, MAX_PEOPLE):
    ppl.append(read_people(f))
  room["people"] = ppl
  objs = []
  for i in range(0, MAX_OBJS):
    objs.append(read_integer(f))
  room["objs"] = objs
  obj_hide = []
  for i in range(0, MAX_OBJS):
    obj_hide.append(read_integer(f))
  room["gold_here"] = read_integer(f)
  room["obj_hides"] = obj_hide
  exit_blocked = []
  for i in range(0, MAX_EXIT):
    exit_blocked.append(read_integer(f))
  room["exit_blocked"] = exit_blocked
  room["extra1"] = read_integer(f)
  return room