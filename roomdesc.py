from exit import *
from read import *

# RoomDesc = RECORD
#   Special_Act :INTEGER;
#   Owner :VeryShortString; { who owns the room }
#   NiceName  :String;  { pretty name for location }
#   NamePrint :INTEGER; { Preposition for room name printing }
#   Primary :INTEGER; { room descriptions }
#   Secondary :INTEGER;       { another description }
#   Which :INTEGER; { Which descrip prints prim and/or secondary }
#   Special_Effect:INTEGER;     { A special effect for this room (block file) }
#   MagicObj  :INTEGER; { special object for this room }
#   Parm  :INTEGER;
#   Exits :ARRAY [1..MaxExit] of Exit;  (* The exits *)
#   ObjDrop :INTEGER; { where objects go when they're dropped }
#   ObjDesc :INTEGER; { what it says when they're dropped }
#   ObjDest :INTEGER; { what it says in target room when
#           "bounced" object comes in }
#   Window  :ARRAY [1..MaxWindow] of INTEGER; { what rooms I can see into }
#   WindowDesc  :ARRAY [1..MaxWindow] of INTEGER; { what it says }
#   Detail  :ARRAY [1..MaxDetail] of VeryShortString;
#   DetailDesc  :ARRAY [1..MaxDetail] of INTEGER;
#   TrapTo  :INTEGER; { where the "trapdoor" goes }
#   TrapChance  :INTEGER; { how often the trapdoor works }
#   RndMsg  :INTEGER; { message that randomly prints }
#   Xmsg2 :INTEGER; { another random block }
#   SpcRoom :INTEGER; { special type of room }
#   Extra1  :INTEGER; { Special type magnitude!}
#   ExitFail  :INTEGER; { default fail description for exits }
#   OFail :INTEGER; { what other's see when you fail, default }
#   ExitAlignment : INTEGER;    { Bitpacked alignment of room exits }
#   DUMMYSPARE    : ARRAY [1..MaxExit] OF INTEGER;
#   Alignment   : INTEGER;  { Bitpacked alignment of room itself }
#   RandomShow  : INTEGER;
#   Extra2  : INTEGER;
#   Mag : ARRAY [0..31] of INTEGER;
# END;

# maxexit = 6;    { 6 exits from each loc: NSEWUD }
MAX_EXIT = 6
# maxwindow = 2;       (* How many windows there can be in a room *)
MAX_WINDOW = 2
# maxdetail = 5;    { max num of detail keys/descriptions per room }
MAX_DETAIL = 5

# Direct : ARRAY[1..MaxExit] OF String :=
#         ('north','south','east','west','up','down');
#SLOT_DIRECTIONS = ['unknown', 'north', 'south', 'east', 'west', 'up', 'down']

EXIT_DIRECTIONS = ['north', 'south', 'east', 'west', 'up', 'down']
SLOT_DIRECTIONS = ['unknown', 'south', 'north', 'west', 'east', 'down', 'up']


def read_roomdesc(f):
  """Should be 812 bytes."""
  roomdesc = {}
  roomdesc["special_act"] = read_integer(f)
  roomdesc["owner"] = read_very_short_string(f)
  roomdesc["nice_name"] = read_string(f)
  roomdesc["name_print"] = read_integer(f)
  roomdesc["primary"] = read_integer(f)
  roomdesc["secondary"] = read_integer(f)
  roomdesc["which"] = read_integer(f)
  roomdesc["special_effect"] = read_integer(f)
  roomdesc["magic_obj"] = read_integer(f)
  roomdesc["parm"] = read_integer(f)
  roomdesc["exits"] = []
  for i in range(0, MAX_EXIT):
    exit = read_exit(f)
    exit["direction"] = EXIT_DIRECTIONS[i]
    #if exit["to_loc"] > 0:
    #  roomdesc["exits"].append(exit)
    roomdesc["exits"].append(exit)
  roomdesc["obj_drop"] = read_integer(f)
  roomdesc["obj_desc"] = read_integer(f)
  roomdesc["obj_dest"] = read_integer(f)
  roomdesc["windows"] = []
  for k in range(0, MAX_WINDOW):
    window = read_integer(f)
    if window > 0:
      roomdesc["windows"].append(window)
  roomdesc["window_descs"] = []
  for l in range(0, MAX_WINDOW):
    window_desc = read_integer(f)
    if window_desc > 0:
      roomdesc["window_descs"].append(window_desc)
  roomdesc["details"] = []    
  for m in range(0, MAX_DETAIL):
    detail = read_very_short_string(f)
    if len(detail) > 0:
      roomdesc["details"].append(detail)
  roomdesc["detail_descs"] = []    
  for n in range(0, MAX_DETAIL):
    detail_desc = read_integer(f)
    if detail_desc > 0:
      roomdesc["detail_descs"].append(detail_desc)
  trap_to = read_integer(f)
  roomdesc["trap_to"] = trap_to
  if trap_to:
    roomdesc["trap_direction"] = EXIT_DIRECTIONS[trap_to - 1]
  roomdesc["trap_chance"] = read_integer(f)
  roomdesc["rnd_msg"] = read_integer(f)
  roomdesc["x_msg_2"] = read_integer(f)
  roomdesc["spc_room"] = read_integer(f)
  roomdesc["extra1"] = read_integer(f)
  roomdesc["exit_fail"] = read_integer(f)
  roomdesc["o_fail"] = read_integer(f)
  roomdesc["exit_alignment"] = read_integer(f)
  roomdesc["dummy_spares"] = []
  for o in range(0, MAX_EXIT):
    dummy_spare = read_integer(f)
    if dummy_spare > 0:
      roomdesc["dummy_spares"].append(dummy_spare)
  roomdesc["alignment"] = read_integer(f)
  roomdesc["random_show"] = read_integer(f)
  roomdesc["extra2"] = read_integer(f)
  roomdesc["magnitudes"] = []
  for p in range(0, 32):
    # the magnitude array is like a bitmask;
    # we need all values to find a given mag at an index position
    roomdesc["magnitudes"].append(read_integer(f))
  return roomdesc
