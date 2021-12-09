# 9.1
import numpy as np
with open('input.txt') as f:
  lines = f.read().splitlines()

def split_string(string):
  return [int(char) for char in string]

def check_adjacent(tubes, row, col):
  if col == 0:
    # Check right only
    if tubes[row][col] >= tubes[row][col+1]:
      return False
  elif col == len(tubes[row])-1:
    # Check left only
    if tubes[row][col] >= tubes[row][col-1]:
      return False
  else:
    if tubes[row][col] >= tubes[row][col-1] or tubes[row][col] >= tubes[row][col+1]:
      return False

  if row == 0:
    # Check down only
    if tubes[row][col] >= tubes[row+1][col]:
      return False
  elif row == len(tubes)-1:
    # Check up only
    if tubes[row][col] >= tubes[row-1][col]:
      return False
  else:
    if tubes[row][col] >= tubes[row-1][col] or tubes[row][col] >= tubes[row+1][col]:
      return False

  return True

low_points = []
lava_tubes = []
for line in lines:
  lava_tubes.append(split_string(line))

for i in range(len(lava_tubes)):
  for j in range(len(lava_tubes[i])):
    lower = check_adjacent(lava_tubes, i, j)
    if lower:
      print('Location: [' + str(i) + ', ' + str(j) + ']')
      low_points.append(lava_tubes[i][j])

result = sum(low_points) + len(low_points)
print('Low points: ' + str(low_points))
print('Results = ' + str(result))
