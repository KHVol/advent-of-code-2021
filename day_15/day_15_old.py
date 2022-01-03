# 15.1
class Move:
  def __init__(self, index, path_size):
    self.index = index
    self.path_size = path_size
  def __str__(self) -> str:
    return f'Index: {self.index}\nPath Size: {self.path_size}\n'

risk_map = []
moves = []

with open('input.txt') as f:
  lines = f.read().splitlines()

for line in lines:
  for i, v in enumerate(line):
    risk_map.append(int(v))

visited = [False] * len(risk_map)
row_length = len(lines[0])
shortest = Move(0, 10000)

# Remove shortest and return a move from the stack
def remove_shortest():
  for i in range(len(moves)):
    if moves[i].index == shortest.index:
      moves.pop(i)
      return

def update_move(i, path):
  for move in moves:
    if move.path_size < shortest.path_size:
      shortest.index = move.index
      shortest.path_size = move.path_size
    if move.index == i and path < move.path_size:
      move.path_size = path
  # If move does not exist in move list add it
  moves.append(Move(i, path))
  return shortest

def check_adjacent(node):
  path = visited[node.index]
  size = len(risk_map)
  if node.index + 1 < size and not visited[node.index+1]:
    # print("Add right")
    node = update_move(node.index+1, path + risk_map[node.index+1])
  if node.index - 1 >= 0 and not visited[node.index-1]:
    # print("Add left")
    node = update_move(node.index-1, path + risk_map[node.index-1])
  if node.index + row_length < size and not visited[node.index+row_length]:
    # print("Add down")
    node = update_move(i+row_length, path + risk_map[node.index+row_length])
  if node.index - row_length >= 0 and not visited[node.index-row_length]:
    # print("Add up")
    node = update_move(node.index-row_length, path + risk_map[node.index-row_length])

  return node

visited[0] = 0
node = check_adjacent(Move(0, 10000))
shortest = node

while len(moves) > 0:
  print(node)
  # whatever is shortest on moves list mark visited
  visited[node.index] = node.path_size
  # remove short node from moves list AND update shortest to be something on stack
  remove_shortest()
  shortest = moves[0]
  # calculate shortest when updating move/checking adjacent
  node = check_adjacent(node)
