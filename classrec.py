from read import *

# ClassRec = RECORD
#   Group : INTEGER;(* What group is this type *)
#   Name,        (* What name is it on the sheet *)
#   WhoName : ShortString; (* What do others see as the name *)
#   BaseHealth, (* MAX health at level 0 *)
#   LevelHealth,    (* Health this class gets per level *)
#   BaseMana, (* Mana this class has at level 0 *)
#   LevelMana,    (* Mana this class gets per level *)
#   BaseSteal,  (* What percent of the time can i steal *)
#   LevelSteal,     (* How good my steal increases per level *)
#   MoveSilent,     (* How good this class moves through shadows *)
#   MoveSilentLevel,(* How much the move silent raises per level *)
#   MoveSpeed,      (* How fast ths class is *)
#   AttackSpeed,    (* How fast can this class hit other players *)
#   HealSpeed,      (* How fast does this class heal *)
#   BaseDamage,     (* The minimum the 'claws' do at level 0 *)
#   RndDamage,      (* How much more can I attach with claws for *)
#   LevelDamage,    (* How much the claws raise per level *)
#   Armor,          (* The base armor for this class *)
#   ExpAdd,         (* How much exp. this class gives to other's *)
#   WeaponUse,      (* How good is the class with a weapon *)
#               LevelWeaponUse,
#   Size,           (* How big is this class *)
#   HearNoise,      (* How good at over hearing things *)
#   PoisonChance, (* How often does this class poison other's *)
#   Control,        (* How well can it control it's actions *)
#   MyVoid,         (* Where do this class go when I dies *)
#   SpellArmor,     (* How much protection against spells *)
#   MonsterType,    (* Generally used just for randoms *)
#                               (* This is a bit mask to determine the *)
#                               (* actions of the random. *)
#   Alignment,
#   HideDelay,
#   ShadowDamagePercent,
#   P1, P2 : INTEGER;
# END;

def read_classrec(f):
  cr = {}
  cr['group'] = read_integer(f)
  cr['name'] = read_short_string(f)
  cr['who_name'] = read_short_string(f)
  cr['base_health'] = read_integer(f)
  cr['level_health'] = read_integer(f)
  cr['base_mana'] = read_integer(f)
  cr['level_mana'] = read_integer(f)
  cr['base_steal'] = read_integer(f)
  cr['level_steal'] = read_integer(f)
  cr['move_silent'] = read_integer(f)
  cr['level_move_silent'] = read_integer(f)
  cr['move_speed'] = read_integer(f)
  cr['attack_speed'] = read_integer(f)
  cr['heal_speed'] = read_integer(f)
  cr['base_damage'] = read_integer(f)
  cr['rnd_damage'] = read_integer(f)
  cr['level_damage'] = read_integer(f)
  cr['armor'] = read_integer(f)
  cr['exp_add'] = read_integer(f)
  cr['weapon_use'] = read_integer(f)
  cr['size'] = read_integer(f)
  cr['hear_noise'] = read_integer(f)
  cr['poison_chance'] = read_integer(f)
  cr['control'] = read_integer(f)
  cr['my_void'] = read_integer(f)
  cr['spell_armor'] = read_integer(f)
  cr['monster_type'] = read_integer(f)
  cr['alignment'] = read_integer(f)
  cr['hide_delay'] = read_integer(f)
  cr['shadow_damage_percent'] = read_integer(f)
  cr['p1'] = read_integer(f)
  cr['p2'] = read_integer(f)
  # TODO: what are the extra 4 bytes?
  f.read(4)
  return cr