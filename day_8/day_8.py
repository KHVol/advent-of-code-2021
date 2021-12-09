# 8.1
with open('input.txt') as f:
  lines = f.read().splitlines()

# total = 0

# for line in lines:
#   signal_pattern, output_value = line.split('|')
#   digits = output_value.split(' ')
#   for digit in digits:
#     if len(digit) in [2, 3, 4, 7]:
#       total += 1

# print(total)

# 8.2
def does_contain(small, large):
  small_array = set(sorted(small))
  large_array = set(sorted(large))
  # print(str(small_array) + " in " + str(large_array))
  if small_array.issubset(large_array):
    return True
  else:
    return False

def is_same(a1, a2):
  if sorted(a1) == sorted(a2):
    return True
  else:
    return False

total = 0
for line in lines:
  signal_pattern, output_value = line.split('|')
  digits = list(filter(None, output_value.split(' ')))
  signal = list(filter(None, signal_pattern.split(' ')))
  an_clock = [''] * 10
  remove = []

  # Find 1, 4, 7, 8 place them in correct position in an_clock array. [X, 1, X, X, 4, X, X, 7, 8, X]
  for i in range(len(signal)):
    if len(signal[i]) == 2:
      an_clock[1] = signal[i]
    elif len(signal[i]) == 3:
      an_clock[7] = signal[i]
    elif len(signal[i]) == 4:
      an_clock[4] = signal[i]
    elif len(signal[i]) == 7:
      an_clock[8] = signal[i]

  # Find 3 which is 1 string + 3 characters. [X, 1, X, 3, 4, X, X, 7, 8, X]
  for i in range(len(signal)):
    if len(signal[i]) == len(an_clock[1]) + 3:
      if does_contain(an_clock[1], signal[i]):
        an_clock[3] = signal[i]
  # Find 9 which is 3 string + 1 character. [X, 1, X, 3, 4, X, X, 7, 8, 9]
  for i in range(len(signal)):
    if len(signal[i]) == 6:
      if does_contain(an_clock[3], signal[i]):
        an_clock[9] = signal[i]
  # Find 0 and 6. 0 has length of 6 with 1's characters. 6 is missing a 1 character. [0, 1, X, 3, 4, X, 6, 7, 8, 9]
  for i in range(len(signal)):
    if len(signal[i]) == 6:
      if does_contain(an_clock[1], signal[i]):
        an_clock[0] = signal[i]
      else:
        an_clock[6] = signal[i]
  # Find 5 which is 6 string - 1 character. [0, 1, X, 3, 4, 5, 6, 7, 8, 9]
  for i in range(len(signal)):
      if len(signal[i]) == 5:
        if does_contain(signal[i], an_clock[6]):
          an_clock[5] = signal[i]
  # Find 2 which is only string left. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  an_clock[2] = list(set(signal).difference(set(an_clock)))[0]
  print(an_clock)

  # Calculate
  num_str = ''
  for digit in digits:
    for i in range(len(an_clock)):
      if is_same(digit, an_clock[i]):
        num_str += str(i)

  total += int(num_str)

print(total)
