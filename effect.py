from read import *

# EffectRec = RECORD
#   Effect  :INTEGER;   (* What type of effect is it *)
#   Name    :ShortString; (* The name of the effect *)
#   All   :BYTE_BOOL;   (* Does it hurt everyone in the room *)
#   Caster  :BYTE_BOOL;   (* Does it hurt the caster *)
#   Prompt  :BYTE_BOOL;   (* Does it ask for user input *)
#   M1,M2,M3,M4 :INTEGER;   (* The magnitude of this effect *)
#  END;

# {Spell Mnemonics}
# sp_cure   =1;
# sp_strength =2;
# sp_speed  =3;
# sp_invisible  =4;
# sp_seeinvisible =5;
# sp_heal   =6;
# sp_hurt   =7;
# sp_sleep  =8;
# sp_push   =9;
# sp_announce =10;
# sp_command  =11;
# sp_dist   =12;
# sp_whatis =13;
# sp_find_person  =14;
# sp_locate =15;
# sp_weak         =16;
# sp_slow         =17;

# Writeln('1)  Cure poison');
# Writeln('2)  Strength');
# Writeln('3)  Speed');
# Writeln('4)  Invisibility');
# Writeln('5)  See invisible');
# Writeln('6)  Heal');
# Writeln('7)  Hurt');
# Writeln('8)  Sleep');
# Writeln('9)  Push');
# Writeln('10) Announce');
# Writeln('11) Command (Warning: Executes with privs)');
# Writeln('12) Distance hurt');
# Writeln('13) Detect magic');
# Writeln('14) Find person');
# Writeln('15) Locate ');
# Writeln('16) Weak');
# Writeln('17) Slow');

def read_effect(f):
  effect = {}
  # effect_int = read_integer(f)
  # if effect_int > 0 and effect_int < len(SPELL_EFFECTS) - 1:
  #   effect['effect'] = SPELL_EFFECTS[effect_int]
  # else:
  #   # empty record or bad data
  #   effect['effect'] = 'UNKNOWN'
  effect['effect'] = read_integer(f)
  effect['name'] = read_short_string(f)
  effect['all'] = read_bytebool(f)
  effect['caster'] = read_bytebool(f)
  effect['prompt'] = read_bytebool(f)
  effect['m1'] = read_integer(f)
  effect['m2'] = read_integer(f)
  effect['m3'] = read_integer(f)
  effect['m4'] = read_integer(f)
  return effect
