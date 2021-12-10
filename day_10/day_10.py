# 10.1
def check_pairs(line: str):
  open = ['[', '{', '(', '<']
  closed = [']', '}', ')', '>']
  stack = []

  for i in range(len(line)):
    if line[i] in open:
      # Open brace push
      stack.append(line[i])
    elif line[i] in closed:
      # Close brace, check if previous is cooresponding open.
      prev_open = stack.pop()
      if open.index(prev_open) != closed.index(line[i]):
        # Bad close brace
        return line[i]
  return

with open('input.txt') as f:
  lines = f.read().splitlines()

total = 0
incomplete = []
for line in lines:
  brace = check_pairs(line)
  if brace == ')':
    total += 3
  elif brace == ']':
    total += 57
  elif brace == '}':
    total += 1197
  elif brace == '>':
    total += 25137
  else:
    incomplete.append(line)

print(total)

# 10.2
def check_incomplete(line: str):
  open = ['[', '{', '(', '<']
  closed = [']', '}', ')', '>']
  stack = []

  for i in range(len(line)):
    if line[i] in open:
      # Open brace push
      stack.append(line[i])
    elif line[i] in closed:
      # Close brace, bad lines are already removed.
      stack.pop()

  return stack

totals = []
open = ['(', '[', '{', '<']
for line in incomplete:
  score = 0
  inc_list = check_incomplete(line)
  # Reverse order cause its how brackets close
  for item in inc_list[::-1]:
    score = (score * 5) + open.index(item) + 1
  totals.append(score)

middle = int((len(totals) -1)/2)
print(sorted(totals)[middle])
