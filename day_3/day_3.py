# 3.1
gamma_rate = ''
epsilon_rate = ''

with open('input.txt') as f:
  lines = f.read().splitlines()

div = len(lines) / 2

for idx in range(len(lines[0])):
  value = 0
  for line in lines:
    value += int(line[idx])
  gamma_rate += '1' if value >= div else '0'
  epsilon_rate += '1' if value < div else '0'

output = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(gamma_rate + ' * ' + epsilon_rate + ' = ' + str(output))

# 3.2
ogr = ''
csr = ''

for idx in range(len(lines[0])):
  ogr_value = 0
  ogr_total = 0
  csr_value = 0
  csr_total = 0

  for line in lines:
    if line.startswith(ogr):
      ogr_value += int(line[idx])
      ogr_total += 1
    if line.startswith(csr):
      csr_value += int(line[idx])
      csr_total += 1

  if ogr_total == 1:
    ogr += line[idx]
  elif ogr_value >= (ogr_total / 2):
    ogr += '1'
  else:
    ogr += '0'

  if csr_total == 1:
    csr += line[idx]
  elif csr_value < (csr_total / 2):
    csr += '1'
  else:
    csr += '0'

life_support = int(ogr, 2) * int(csr, 2)
print(ogr + ' * ' + csr + ' = ' + str(life_support))
