from read import *
from saying import *

# type
#   RandREC = RECORD
#     Name          :String;  (* The name of this type of random monster *)
#     BaseHealth    :INTEGER; (* The base health for this random type *)
#     RandomHealth  :INTEGER; (* The level health for this type *)
#     BaseDamage    :INTEGER; (* The base damage of this type *)
#     RandomDamage  :INTEGER; (* The random damage of this type *)
#     LevelDamage   :INTEGER; (* The level damage *)
#     Armor         :INTEGER; (* What percent armor this type of random has *)
#     SpellArmor    :INTEGER; (* Spell armor for this type *)
#     MoveSpeed     :INTEGER; (* How fast is this random *)
#     AttackSpeed   :INTEGER; (* attack speed ... *)
#     Kind          :INTEGER; (* What type of random is it *)
#     Experience    :INTEGER; (* How much experience does it give when killed *)
#     Gold          :INTEGER; (* What is the max amount of gold it carrries *)
#     MinLevel      :INTEGER; (* At what level do they start appearing *)
#     HealSpeed     :INTEGER; (* How fast does itheal *)
#     Spell         :ARRAY [1..MaxRandomSpells] of INTEGER; (* spells it has *)
#     LevelHealth   :INTEGER;
#     Extra1, Extra2:INTEGER;
#     Group         :INTEGER; (* What group does it belong to *)
#     PursuitChance :INTEGER; (* How often does it follow *)
#     WeaponUse     :INTEGER;  (* What is the name of its weapon *)
#     LevelWeaponUse:INTEGER;
#     Weapon        :INTEGER;
#     Object        :INTEGER; (* What object does it drop when it dies *)
#     Sayings       :ARRAY [1..10] of Saying; (* What can it say *)
#     BaseMana,
#     LevelMana     :INTEGER;
#     Size          :INTEGER;
#   END;

# maxrandomspells = 7;
MAX_RANDOM_SPELLS = 7

def read_random(f):
  r = {}
  r['name'] = read_string(f)
  r['base_health'] = read_integer(f)
  r['random_health'] = read_integer(f)
  r['base_damage'] = read_integer(f)
  r['random_damage'] = read_integer(f)
  r['level_damage'] = read_integer(f)
  r['armor'] = read_integer(f)
  r['spell_armor'] = read_integer(f)
  r['move_speed'] = read_integer(f)
  r['attack_speed'] = read_integer(f)
  r['kind'] = read_integer(f)
  r['experience'] = read_integer(f)
  r['gold'] = read_integer(f)
  r['min_level'] = read_integer(f)
  r['heal_speed'] = read_integer(f)
  r['spells'] = []
  for i in range(0, MAX_RANDOM_SPELLS):
    spell = read_integer(f)
    if spell > 0:
      r['spells'].append(spell)
  r['level_health'] = read_integer(f)
  r['extra1'] = read_integer(f)
  r['extra2'] = read_integer(f)
  r['group'] = read_integer(f)
  r['pursuit_chance'] = read_integer(f)
  r['weapon_use'] = read_integer(f)
  r['level_weapon_use'] = read_integer(f)
  r['weapon'] = read_integer(f)
  r['object'] = read_integer(f)
  r['sayings'] = []
  for j in range(0, 10):
    saying = read_saying(f)
    if len(saying['saying']) > 0:
      r['sayings'].append(saying)
  r['base_mana'] = read_integer(f)
  r['level_mana'] = read_integer(f)
  r['size'] = read_integer(f)
  return r
