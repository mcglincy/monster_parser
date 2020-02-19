#!/usr/bin/python3

import json

# Numeric encoding is little-endian.
#
# An INTEGER is a 4-byte little-endian signed int.
#
# A VARYING array of CHAR is encoded with:
# length: 2-byte short.
# chars: 1-byte ASCII idx for each char up to length
#
# BYTE_BOOL = [BIT] BOOLEAN;
#
# veryshortlen = 12;  { very short string length for userid's etc }
# shortlen = 20;    { ordinary short string }
# normlen = 80;           { normal string length }
#
# String = VARYING[NormLen] of CHAR;
# ShortString = VARYING[ShortLen] of CHAR;
# VeryShortString = VARYING[VeryShortLen] of CHAR;
#
# maxexit = 6;    { 6 exits from each loc: NSEWUD }
# maxwindow = 2;       (* How many windows there can be in a room *)
# maxdetail = 5;    { max num of detail keys/descriptions per room }

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

BYTE_ORDER = 'little'
MAX_EXIT = 6
MAX_WINDOW = 2
MAX_DETAIL = 5
EXIT_DIRECTIONS = ['north', 'south', 'east', 'west', 'up', 'down']

def read_bytebool(f):
  # TODO: parse BYTE_BOOL
  return int.from_bytes(f.read(1), byteorder=BYTE_ORDER)

def read_integer(f):
  """Returns 4-byte int."""
  return int.from_bytes(f.read(4), byteorder=BYTE_ORDER)

def read_varying_char(f, max_length):
  length = int.from_bytes(f.read(2), byteorder=BYTE_ORDER)
  max_bytes = f.read(max_length)
  if length == 0:
    return ''
  char_bytes = max_bytes[0:length]
  chars = [str(chr(b)) for b in char_bytes]
  return ''.join(chars)

def read_string(f):
  return read_varying_char(f, 80)

def read_short_string(f):
  return read_varying_char(f, 20)

def read_very_short_string(f):
  return read_varying_char(f, 12)

def read_exit(f):
  exit = {}
  exit["to_loc"] = read_integer(f)
  exit["kind"] = read_integer(f)
  exit["slot"] = read_integer(f)
  exit["exit_desc"] = read_integer(f)
  exit["door_effect"] = read_integer(f)
  exit["fail"] = read_integer(f)
  exit["success"] = read_integer(f)
  exit["goin"] = read_integer(f)
  exit["come_out"] = read_integer(f)
  exit["hidden"] = read_integer(f)
  exit["obj_req"] = read_integer(f)
  exit["alias"] = read_very_short_string(f)
  exit["req_verb"] = read_bytebool(f)
  exit["req_alias"] = read_bytebool(f)
  exit["auto_look"] = read_bytebool(f)
  return exit

def read_roomdesc(f):
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
  for j in range(0, MAX_EXIT):
    exit = read_exit(f)
    exit["direction"] = EXIT_DIRECTIONS[j]
    if exit["to_loc"] > 0:
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
  roomdesc["trap_to"] = read_integer(f)
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
  roomdesc["mags"] = []
  for p in range(0, 32):
    mag = read_integer(f)
    if mag > 0:
      roomdesc["mags"].append(mag)
  return roomdesc


filename = 'roomdesc.mon'
with open(filename, 'rb') as f:
  roomdescs = []
  # 752
  for i in range(0, 752):
    roomdesc = read_roomdesc(f)
    roomdescs.append(roomdesc)
  print(json.dumps(roomdescs, indent = 2, sort_keys=False))



