# 25.1
import numpy as np
with open('input.txt') as f:
  lines = f.read().splitlines()

def print_map(my_map):
  print(str('-' * len(my_map)))
  for row in my_map:
    str_row = ''
    for col in row:
      str_row += col
    print(str_row)
  print(str('-' * len(my_map)))

def east_move(my_map, char):
  any_moves = False
  for row in range(len(my_map)):
    moves = np.where(my_map[row] == char)[0]
    for move in moves:
      col = (move + 1) % len(my_map[row])
      if my_map[row][col] == '.':
        any_moves = True
        my_map[row][col] = char
        my_map[row][move] = '.'
  return my_map, any_moves

def south_move(my_map):
  any_moves = False
  for col in range(len(my_map[0])):
    moves = np.where(my_map[:,col] == 'v')[0]
    for move in moves:
      row = (move + 1) % len(my_map[:,col])
      if my_map[row][col] == '.':
        any_moves = True
        my_map[row][col] = 'v'
        my_map[move][col] = '.'
  return my_map, any_moves

# Build cucumber map
cuc_map = []
for x in range(len(lines)):
  arr = []
  for y in range(len(lines[x])):
    arr.append(lines[x][y])
  cuc_map.append(arr)
cuc_map = np.array(cuc_map)

east_moves = True
south_moves = True
total_moves = 0
print_map(cuc_map)

while east_moves or south_moves:
  cuc_map, east_moves  = east_move(cuc_map, '>')
  cuc_map, south_moves = south_move(cuc_map)
  print_map(cuc_map)
  total_moves += 1

print_map(cuc_map)
print(total_moves)
