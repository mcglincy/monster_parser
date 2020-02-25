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
  # spell deflect aka spell destroy
  SPELL_DEFLECT_ARMOR = 39
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


def camel_case(s):
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


def snake_case(s):
  """Convert an object name to a snake case.

  E.g., 'Hammer of the gods' => 'HAMMER_OF_THE_GODS'
  """
  s = s.strip()
  chars = []
  for c in s:
    if c == ' ' or c == '-':
      chars.append('_')
    elif c == "'":
      pass
    else:
      chars.append(c.upper())
  return ''.join(chars)


def escaped(s):
  return s.replace('"', '\\"')


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
    if (lookup_effect(obj, Effect.WEAPON_BASE_DAMAGE)
      or lookup_effect(obj, Effect.WEAPON_RANDOM_DAMAGE)):
      weapons.append(obj)
    elif (lookup_effect(obj, Effect.BASE_ARMOR)
      or lookup_effect(obj, Effect.DEFLECT_ARMOR)
      or lookup_effect(obj, Effect.SPELL_ARMOR)):
      armor.append(obj)
weapons.sort(key=lambda x: x['obj_name'].upper())
armor.sort(key=lambda x: x['obj_name'].upper())

print("""
#
# Weapon prototypes
#

WEAPON = {
  'typeclass': 'typeclasses.objects.Weapon',
  'key': 'weapon',
  'attack_speed': 0,
  'base_damage': 0,
  'desc': 'A weapon.',
  'equip_slot': 1,
  'random_damage': 0,
  'weight': 0,
  'worth': 0
}
""")

for weapon in weapons:
#  classname = camelcase_class_name(weapon['obj_name'])
#  print(f'class {classname}(Weapon):')
#  print('  pass')
  obj_name = weapon['obj_name']
  base_damage = lookup_effect(weapon, Effect.WEAPON_BASE_DAMAGE) or 0
  random_damage = lookup_effect(weapon, Effect.WEAPON_RANDOM_DAMAGE) or 0
  attack_speed = lookup_effect(weapon, Effect.ATTACK_SPEED) or 0
  print(f"{snake_case(obj_name)} = {{")
  # TODO: add better quote escaping for key and desc
  print(f"  'key': \"{weapon['obj_name']}\",")
  print("  'prototype_parent': 'WEAPON',")
  print(f"  'attack_speed': {attack_speed},")
  print(f"  'base_damage': {base_damage},")
  desc_idx = weapon['examine'] - 1
  if desc_idx >= 0 and desc_idx < len(descs):
    # TODO: special handling for 'default' descript 32000
    desc = escaped(' '.join(descs[desc_idx]['lines']))
    print(f"  'desc': \"{desc}\",")
  print(f"  'equip_slot': {weapon['wear']},")
  # TODO: handle line_desc? looks mostly dead
  print(f"  'random_damage': {random_damage},")
  print(f"  'weight': {weapon['weight']},")
  print(f"  'worth': {weapon['worth']},")
  print('}')
  print()


print("""
#
# Armor prototypes
#

ARMOR = {
  'typeclass': 'typeclasses.objects.Armor',
  'key': 'armor',
  'base_armor': 0,
  'deflect_armor': 0,
  'desc': 'An armor.',
  'equip_slot': 4,
  'spell_armor': 0,
  'spell_deflect_armor': 0,
  'weight': 0,
  'worth': 0  
}
""")

for armor in armor:
  obj_name = armor['obj_name']
  base_armor = lookup_effect(armor, Effect.BASE_ARMOR) or 0
  deflect_armor = lookup_effect(armor, Effect.DEFLECT_ARMOR) or 0
  spell_armor = lookup_effect(armor, Effect.SPELL_ARMOR) or 0
  spell_deflect_armor = lookup_effect(armor, Effect.SPELL_DEFLECT_ARMOR) or 0
  print(f"{snake_case(obj_name)} = {{")  
  # TODO: add better quote escaping for key and desc
  print(f"  'key': \"{armor['obj_name']}\",")
  print("  'prototype_parent': 'ARMOR',")
  print(f"  'base_armor': {base_armor},")  
  print(f"  'deflect_armor': {deflect_armor},")  
  desc_idx = armor['examine'] - 1
  if desc_idx >= 0 and desc_idx < len(descs):
    # TODO: special handling for 'default' descript 32000
    desc = escaped(' '.join(descs[desc_idx]['lines']))
    print(f"  'desc': \"{desc}\",")
  print(f"  'equip_slot': {armor['wear']},")  
  # TODO: handle line_desc? looks mostly dead
  print(f"  'spell_armor': {spell_armor},")  
  print(f"  'spell_deflect_armor': {spell_deflect_armor},")  
  print(f"  'weight': {armor['weight']},")  
  print(f"  'worth': {weapon['worth']},")  
  print('}')
  print()
