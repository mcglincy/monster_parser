
# Numeric encoding is little-endian.
BYTE_ORDER = 'little'

# normlen = 80;           { normal string length }
STRING_LENGTH_NORMAL = 80
# shortlen = 20;    { ordinary short string }
STRING_LENGTH_SHORT = 20
# veryshortlen = 12;  { very short string length for userid's etc }
STRING_LENGTH_VERY_SHORT = 12


def has_more_data(f):
  offset = f.tell()
  b = f.read(1)
  if b == b"":
    return False
  # go back to where we were
  f.seek(offset, 0)
  return True

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
  """Read a normal ASCII string.

  82 bytes total (2 len + 80 chars)

  String = VARYING[NormLen] of CHAR;
  """
  return read_varying_char(f, STRING_LENGTH_NORMAL)

def read_short_string(f):
  """Read a short ASCII string.

  22 bytes total (2 len + 20 chars)

  ShortString = VARYING[ShortLen] of CHAR;
  """
  return read_varying_char(f, STRING_LENGTH_SHORT)

def read_very_short_string(f):
  """Read a very short ASCII string.

  14 bytes total (2 len + 12 chars)

  VeryShortString = VARYING[VeryShortLen] of CHAR;
  """
  return read_varying_char(f, STRING_LENGTH_VERY_SHORT)

