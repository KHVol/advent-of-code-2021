# 7.1
import numpy as np

crab_pos = [16,1,2,0,4,2,7,1,2,14]
med = np.median(crab_pos)

fuel = 0

for pos in crab_pos:
  fuel += abs(pos - med)

print(fuel)

# 7.2
def triangular_number(n):
  return n * (n + 1)

# We have to change what converge point is because high numbers are now weighted more.

