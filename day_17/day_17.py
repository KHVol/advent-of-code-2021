# 17.1
import numpy as np
x_target = np.arange(179, 201+1, 1)
y_target = np.arange(-109, -63+1, 1)

def nth_triangle(n) -> int:
  return (n * (n+1)) / 2

def triangle_number(n) -> int:
  return ((np.sqrt(8*n + 1) - 1) / 2)

def smallest_triangle(target_array) -> int:
  for i in target_array:
    if triangle_number(i).is_integer():
      return triangle_number(i)

def largest_triangle(target_array) -> int:
  largest = 0
  for i in target_array:
    if triangle_number(i).is_integer():
      largest = i
  return largest

def in_x_target(x) -> bool:
  if x in x_target:
    return True
  return False

def in_y_target(y) -> bool:
  if y in y_target:
    return True
  return False

def in_target(x, y) -> bool:
  return in_x_target(x) and in_y_target(y)

def land_in_target(y) -> bool:
  # Finding y requires getting the nth triangle which will be the max height.
  n = nth_triangle(y)
  remove = 0
  # Loop until y is in target area or past target area.
  while n > min(y_target):
    remove += 1
    n = n - remove
    if in_y_target(n):
      return True
  return False

def y_landing_spot(y) -> int:
  # Finding y requires getting the nth triangle which will be the max height.
  n = nth_triangle(y)
  remove = 0
  # Loop until y is in target area or past target area.
  while n > min(y_target):
    remove += 1
    n = n - remove
    if in_y_target(n):
      return n
  return n

# Find smallest x. (Smallest y gives us the most time to go up and come back down)
# x_coord = smallest_triangle(x_target)

# # Start at 0 and go up until y is out of bounds
# y_max = 0
# y_coord = 0
# for y in range(1000): # This is a brute force which is pretty terrible.
#   land = land_in_target(y)
#   if land and y > y_max:
#       y_max = y
#       y_coord = y

# print(x_coord, y_coord)
# print(nth_triangle(y_coord))

# nth_triangle()
# Then working down until in the target zone.
# Make sure that x and y are both within target zone.
# What is reverse nth triangle
# We want to go from 45 backwards til in target zone so,
# 45.44..42...39....35.....30......24.......17........9.........0...........-10
# 6.5..3...0....-4....-9
# 36.35..33...30....26.....21......15.......8.......0........-9

# 17.2
# y = lowest_number(-109)...highest_number(108)
# y_min = 0
# y_coord = 0
# for y in range(-1000, 0): # This is a brute force which is pretty terrible.
#   land = land_in_target(y)
#   if land and y < y_min:
#       y_min = y
#       y_coord = y

# x = smallest_triangle(19) to largest_triangle(190)
# print(largest_triangle(x_target))

total = 0
for x in range(18, 191):
  for y in range(-109, 108):
    x_landing = nth_triangle(x)
    y_landing = y_landing_spot(y)
    print(x, y)
    if in_target(x_landing, y_landing):
      total += 1

print(total)
