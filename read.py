
# Numeric encoding is little-endian.
BYTE_ORDER = 'little'

def read_bytebool(f):
  """Read a one-byte boolean.

  BYTE_BOOL = [BIT] BOOLEAN; 
  """
  # TODO: parse BYTE_BOOL
  return int.from_bytes(f.read(1), byteorder=BYTE_ORDER)

def read_integer(f):
  """Read an integer.

  An INTEGER is a 4-byte little-endian signed int."""
  return int.from_bytes(f.read(4), byteorder=BYTE_ORDER)

def read_varying_char(f, max_length):
  """Read a VARYING CHAR array as a string.

  A VARYING array of CHAR is encoded with:
  - length: 2-byte short.
  - chars: 1-byte ASCII idx for each char up to length

  VARYING arrays always take up max_length bytes in the file.
  """
  length = int.from_bytes(f.read(2), byteorder=BYTE_ORDER)
  max_bytes = f.read(max_length)
  if length == 0:
    return ''
  char_bytes = max_bytes[0:length]
  chars = [str(chr(b)) for b in char_bytes]
  return ''.join(chars)

def read_string(f):
  """Read a normal string.

  normlen = 80;           { normal string length }
  String = VARYING[NormLen] of CHAR;
  """
  return read_varying_char(f, 80)

def read_short_string(f):
  """Read a short string.

  shortlen = 20;    { ordinary short string }
  ShortString = VARYING[ShortLen] of CHAR;
  """
  return read_varying_char(f, 20)

def read_very_short_string(f):
  """Read a very short string.

  veryshortlen = 12;  { very short string length for userid's etc }
  VeryShortString = VARYING[VeryShortLen] of CHAR;
  """
  return read_varying_char(f, 12)

