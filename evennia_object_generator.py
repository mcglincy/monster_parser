#!/usr/bin/python3

from enum import IntEnum
import json


DESC_FILE = './json/desc.json'
OBJECT_FILE = './json/objects.json'


class ObjectKind(IntEnum):
  BLAND = 0
  EQUIP= 1
  SCROLL = 2
  WAND   = 3
  MISSILE = 7
  MISSILELAUNCHER = 8
  SBOOK = 104
  BANKING_MACHINE = 106


class Effect(IntEnum):
  ATTACK_SPEED = 13
  WEAPON_BASE_DAMAGE = 27
  WEAPON_RANDOM_DAMAGE = 28
  BASE_ARMOR = 29
  DEFLECT_ARMOR = 30
  SPELL_ARMOR = 31
  SMALLEST_FIT = 32
  LARGEST_FIT = 33
  THROW_BASE = 40
  THROW_RANDOM = 41
  THROW_RANGE = 42
  THROW_BEHAVIOR = 43 


def parse_parm(i):
  """Parse a parm integer into the effect and effectnum."""
  return (i % 100, int(i / 100))


def lookup_effect(obj, effect):
  for parm in obj['parms']:
    eff, eff_num = parse_parm(parm)
    if eff == effect:
      return eff_num


def camelcase_class_name(s):
  """Convert an object name to a useful python class name.

  E.g., 'Hammer of the gods' => 'HammerOfTheGods'
  """
  s = s.strip()
  done = False
  chars = []
  idx = 0
  s_len = len(s)
  while not done:
    c = s[idx]
    if idx == 0:
      chars.append(c.upper())
      idx = idx + 1
    elif c == ' ':
      chars.append(s[idx+1].upper())
      idx = idx + 2
    elif c == "'":
      # skip quote
      idx = idx + 1
    else:
      chars.append(c)
      idx = idx + 1
    if idx >= s_len:
      done = True
  return ''.join(chars)


##########


with open(OBJECT_FILE) as f:
  objects = json.load(f)

with open(DESC_FILE) as f:
  descs = json.load(f)

print("""# evmonster generated objects
#
#""")

# divide objects into lists of weapons and armor
weapons = []
armor = []
for obj in objects:
  if obj['kind'] == ObjectKind.EQUIP:
    if lookup_effect(obj, Effect.WEAPON_BASE_DAMAGE):
      weapons.append(obj)
    elif lookup_effect(obj, Effect.BASE_ARMOR):
      armor.append(obj)
weapons.sort(key=lambda x: x['obj_name'])
armor.sort(key=lambda x: x['obj_name'])

print("""
WEAPON_PROTOTYPES = {
  'weapon': {
    'typeclass': 'objects.Weapon',
    'key': 'weapon',
    'description': 'A weapon.',
  },""")
for weapon in weapons:
#  classname = camelcase_class_name(weapon['obj_name'])
#  print(f'class {classname}(Weapon):')
#  print('  pass')
  base_damage = lookup_effect(weapon, Effect.WEAPON_BASE_DAMAGE) or 0
  random_damage = lookup_effect(weapon, Effect.WEAPON_RANDOM_DAMAGE) or 0
  attack_speed = lookup_effect(weapon, Effect.ATTACK_SPEED) or 0
  print(f"  '{weapon['obj_name']}': {{")
  print("    'prototype_parent': 'weapon',")
  print(f"    'base_damage': {base_damage},")
  print(f"    'random_damage': {random_damage},")
  print(f"    'attack_speed': {attack_speed},")
  print(f"    'weight': {weapon['weight']},")
  print(f"    'equip_slot': {weapon['wear']},")
  desc_idx = weapon['examine'] - 1
  if desc_idx >= 0 and desc_idx < len(descs):
    # TODO: special handling for 'default' descript 32000
    desc = ' '.join(descs[desc_idx]['lines'])
    print(f"    'description': '{desc}',")
  # TODO: handle line_desc? looks mostly dead
  print('  },')
print('}')

print("""
ARMOR_PROTOTYPES = {
  'armor': {
    'typeclass': 'objects.Armor',
    'key': 'armor',
    'description': 'An armor.',
  },""")
for armor in armor:
  base_armor = lookup_effect(armor, Effect.BASE_ARMOR) or 0
  deflect_armor = lookup_effect(armor, Effect.DEFLECT_ARMOR) or 0
  spell_armor = lookup_effect(armor, Effect.SPELL_ARMOR) or 0

  print(f"  '{armor['obj_name']}': {{")
  print("    'prototype_parent': 'armor',")
  print(f"    'base_armor': {base_armor},")  
  print(f"    'deflect_armor': {deflect_armor},")  
  print(f"    'spell_armor': {spell_armor},")  
  print(f"    'weight': {armor['weight']},")  
  print(f"    'equip_slot': {weapon['wear']},")  
  #print(f"    'base_damage': {base_damage},")
  desc_idx = weapon['examine'] - 1
  if desc_idx >= 0 and desc_idx < len(descs):
    # TODO: special handling for 'default' descript 32000
    desc = ' '.join(descs[desc_idx]['lines'])
    print(f"    'description': '{desc}',")
  # TODO: handle line_desc? looks mostly dead
  print('  },')
print('}')


#  print(f'class {classname}(Armor):')
#  print('  pass')

#      pass
      # print(obj['obj_name'])
      # print(lookup_effect(obj, Effect.BASE_ARMOR))

      # it's a weapon
      #print(obj['obj_name'])
      #print(lookup_effect(obj, Effect.WEAPON_BASE_DAMAGE))

    # for parm in obj['parms']:
      # print(parse_parm(parm))

print("""#
#
#""")