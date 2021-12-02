# 2.1
position = 0
depth = 0
with open('input.txt') as f:
  lines = f.read().splitlines()

for line in lines:
  dir, num = line.split(' ')
  if dir == 'forward':
    position += int(num)
  elif dir == 'down':
    depth += int(num)
  elif dir == 'up':
    depth -= int(num)

print(position * depth)

# 2.2
aim = 0
position = 0
depth = 0
for line in lines:
  dir, num = line.split(' ')
  if dir == 'forward':
    position += int(num)
    depth += int(num) * aim
  elif dir == 'down':
    aim += int(num)
  elif dir == 'up':
    aim -= int(num)

print(position * depth)
