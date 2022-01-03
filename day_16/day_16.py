# 16.1
def hex_to_binary(hex_string):
  scale = 16
  return bin(int(hex_string, scale))[2:].zfill(8)

with open('input.txt') as f:
  lines = f.read().splitlines()

print(hex_to_binary(lines[0]))

# Type ID 4 = literal value
# Any other type ID is an operator
# Operators have a Length Type ID which is one bit
# If 0 then 15 bit number then length of subpackets in bits
# If 1 then 11 bit number then represents number of subpackets
#
