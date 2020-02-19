from read import *

# AtmosphereREC = RECORD
#   Trigger :ShortString; (* Nonsense commands to print messages on terms*)
#   Isee  :String;      (* What is printed to me when i say trigger *)
#   Eventsee  :String;      (* What others see when i say trigger *)
#   ISeeExtra :String;      (* What I see when i say trigegr # *)
#   EventSeeExtra:String;     (* What others see when i say trigger # *)
#   Owner : ShortString;      (* Who made the atmosphere command up. *)
# END;

def read_atmosphere(f):
  a = {}
  a['trigger'] = read_short_string(f)
  a['i_see'] = read_string(f)
  a['event_see'] = read_string(f)
  a['i_see_extra'] = read_string(f)
  a['event_see_extra'] = read_string(f)
  a['owner'] = read_short_string(f)  
  return a