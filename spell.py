from effect import *
from read import *

# SpellRec = Record
#   Name    :ShortString;   (* The spell's name *)
#   Mana    :INTEGER;       (* How much mana does it cost *)
#   LevelMana :INTEGER;       (* How much mana does it cost/level *)
#   CasterDesc  :INTEGER; (* Index of a desc. block *)
#   VictimDesc  :INTEGER;       (* Index of a desc block *)
#   Alignment :INTEGER;       (* Spell Alignment *)
#   FailureDesc :INTEGER;       (* Index of a desc block *)
#   MinLevel  :INTEGER;       (* Minimum level needed to cast *)
#   Class   :INTEGER;       (* What class casn cast it *)
#   Group   :INTEGER;       (* What group can cast it *)
#   Room    :INTEGER;       (* Where do I have to be to cast it *)
#   Effect  :ARRAY [0..MaxSpellEffect] of EffectRec; (* effects *)
#   ChanceOfFailure:INTEGER;      (* What percent of the time fails *)
#   CastingTime :INTEGER;       (* How long does it take to cast *)
#   ObjRequired :INTEGER;    (* What do I have to be holding to cast *)
#   ObjConsumed :BYTE_BOOL;       (* Is the object destroyed *)
#   Silent  :BYTE_BOOL;    (* Does it tell others I am casting it *)
#   Reveals :BYTE_BOOL;       (* Does it reveal me *)
#   Memorize  :BYTE_BOOL;       (* Do I need to learn it *)
#   Command :String;  (* Command to execute *)
#   CommandPriv :BYTE_BOOL; (* Execute it with Privs? *)
#   Extra1, Extra2, Extra3 : INTEGER;
# END;

# maxspelleffect = 4;  (* How many effects a spell can have *)
MAX_SPELL_EFFECT = 4

def read_spell(f):
  spell = {}
  spell['name'] = read_short_string(f)
  spell['mana'] = read_integer(f)
  spell['level_mana'] = read_integer(f)
  spell['caster_desc'] = read_integer(f)
  spell['victim_desc'] = read_integer(f)
  spell['alignment'] = read_integer(f)
  spell['failure_desc'] = read_integer(f)
  spell['min_level'] = read_integer(f)
  spell['class'] = read_integer(f)
  spell['group'] = read_integer(f)
  spell['room'] = read_integer(f)
  spell['effects'] = []
  # pascal array is 0-specified [0..MaxSpellEffect], which is one more
  for i in range(0, MAX_SPELL_EFFECT + 1):
    effect = read_effect(f)
    if effect['effect'] != 'UNKNOWN':
      spell['effects'].append(effect)
  spell['chance_of_failure'] = read_integer(f)
  spell['casting_time'] = read_integer(f)
  spell['obj_required'] = read_integer(f)
  spell['obj_consumed'] = read_bytebool(f)
  spell['silent'] = read_bytebool(f)
  spell['reveals'] = read_bytebool(f)
  spell['memorize'] = read_bytebool(f)
  spell['command'] = read_string(f)
  spell['command_priv'] = read_bytebool(f)
  spell['extra1'] = read_integer(f)
  spell['extra2'] = read_integer(f)
  spell['extra3'] = read_integer(f)
  return spell