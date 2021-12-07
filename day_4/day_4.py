# 4.1
import numpy as np
from numpy.lib.function_base import append

with open('input.txt') as f:
  boards = f.read().split('\n\n')

drawn_numbers = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]
score = 0
win_len = 1000

def check_win(board, nums):
  # Checks row wins
  for i in range(len(board[0])):
    if all(x in nums for x in board[i]):
      return len(nums)
  # Checks column wins
  for j in range(len(board[0])):
    if all(x in nums for x in board[:,j]):
      return len(nums)

  return -1

def calculate_score(board, nums, win_spot):
  unmarked_spots = 0
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] not in nums:
        unmarked_spots += board[i][j]
  print(str(unmarked_spots) + ' * ' + str(nums[win_spot-1]))
  return unmarked_spots * nums[win_spot-1]

def create_board(str_board: str):
  bingo_board = []
  index = len(str_board)
  for i in range(index):
    row = list(map(int, list(filter(None,(str_board[i].split(' '))))))
    if row:
      bingo_board.append(row)
  return np.array(bingo_board)

# Loop over each board
for str_board in boards:
  bingo_board = create_board(str_board.split('\n'))
  index = 4
  print(bingo_board)

  # Loop over each drawn_number (after row len)
  while index < len(drawn_numbers):
    # Determine which index board wins on
    win_spot = check_win(bingo_board, drawn_numbers[0:index])
    # If quickest win, save the score(total unused * winning number)
    if win_spot > 0 and win_spot < win_len:
      win_len = win_spot
      score = calculate_score(bingo_board, drawn_numbers[0:index], win_spot)
      index = len(drawn_numbers)

    index += 1

  print(score)

# 4.2
score = 0
win_len = 0
# Loop over each board
for str_board in boards:
  bingo_board = create_board(str_board.split('\n'))
  index = 4
  print(bingo_board)

  # Loop over each drawn_number (after row len)
  while index < len(drawn_numbers):
    # Determine which index board wins on
    win_spot = check_win(bingo_board, drawn_numbers[0:index])
    # If quickest win, save the score(total unused * winning number)
    if win_spot > 0:
      if win_spot > win_len:
        win_len = win_spot
        score = calculate_score(bingo_board, drawn_numbers[0:index], win_spot)
      index = len(drawn_numbers)
    index += 1

  print(score)
