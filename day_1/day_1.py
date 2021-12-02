# 1.1
increase = 0
with open('input.txt') as f:
  lines = f.read().splitlines()
for i in range(len(lines)):
  if i > 0 and int(lines[i]) > int(lines[i-1]):
    increase += 1
print("Part 1 - " + str(increase))

# 1.2
total = 0
new_lines = []
for j in range(len(lines) - 2):
  new_lines.append(int(lines[j]) + int(lines[j+1]) + int(lines[j+2]))

for k in range(len(new_lines)):
  if new_lines[k] > new_lines[k-1]:
    total += 1
print("Part 2 - " + str(total))
