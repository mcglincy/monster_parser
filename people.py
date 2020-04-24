from read import *

# PeopleREC = RECORD
#   Kind       : INTEGER;         { Log number of the person in the slot }
#   Targ       : INTEGER;         { who is the npc after? }
#   DEL1       : VeryShortString; { actual userid of person }
#   Name       : ShortString;     { chosen name of person }
#   Hiding     : INTEGER;         { degree to which they're hiding }
#   NextAct    : INTEGER;
#   DEL3 : INTEGER;         { last thing that this person did }
#   DEL4       : BYTE_BOOL;         { Can others see me }
#   Health,
#   DEL5       : INTEGER;
# END;

def read_people(f):
  people = {}
  people["kind"] = read_integer(f)
  people["targ"] = read_integer(f)
  people["del1"] = read_very_short_string(f)
  people["name"] = read_short_string(f)
  people["hiding"] = read_integer(f)
  people["next_act"] = read_integer(f)
  people["del3"] = read_integer(f)
  people["del4"] = read_bytebool(f)
  people["health"] = read_integer(f)
  people["del5"] = read_integer(f)
  return people
