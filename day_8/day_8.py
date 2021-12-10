# 8.1
with open('input.txt') as f:
  lines = f.read().splitlines()

total = 0

for line in lines:
  signal_pattern, output_value = line.split('|')
  digits = output_value.split(' ')
  for digit in digits:
    if len(digit) in [2, 3, 4, 7]:
      total += 1

print(total)

# 8.2
def find_nums(nums):
    n1 = [x for x in nums if len(x) == 2][0]
    n4 = [x for x in nums if len(x) == 4][0]
    n7 = [x for x in nums if len(x) == 3][0]
    n8 = [x for x in nums if len(x) == 7][0]
    n9 = [x for x in nums if len(x) == 6 and all(y in x for y in n4)][0]
    n0 = [x for x in nums if len(x) == 6 and x != n9 and all(y in x for y in n1)][0]
    n6 = [x for x in nums if len(x) == 6 and x != n9 and x != n0][0]
    n3 = [x for x in nums if len(x) == 5 and all(y in x for y in n1)][0]
    n5 = [x for x in nums if len(x) == 5 and x != n3 and all(y in n9 for y in x)][0]
    n2 = [x for x in nums if len(x) == 5 and x != n3 and x != n5][0]
    return [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]


pattern = [[["".join(sorted(z)) for z in y.split()] for y in x.split(" | ")] for x in lines]
result = 0
for nums, digits in pattern:
    nums = find_nums(nums)
    result += int("".join([str(nums.index(x)) for x in digits]))
print(result)
