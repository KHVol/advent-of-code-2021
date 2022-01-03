# 21.1
def player_turn(p_spot, p_score, dice):
  det_dice = dice % 100
  if det_dice == 0:
    det_dice = 100

  move = (det_dice * 3) + 3
  new_spot = (p_spot + move) % 10
  if new_spot == 0:
    new_spot = 10
  new_score = p_score + new_spot
  if check_win(new_score, dice):
    return new_spot, new_score, dice+3, True

  return new_spot, new_score, dice+3, False


def check_win(p_score, dice):
  win = False
  if p_score >= 1000:
    win = True
    det_dice = dice % 100
  else:
    dice += 3
    det_dice = dice % 100
    if det_dice == 0:
      dice = 100

  return win

p1_score = 0
p1_spot = 4
p2_score = 0
p2_spot = 2

dice = 1
result = 0
win = False

while not win:
  # player_1 turn
  p1_spot, p1_score, dice, win = player_turn(p1_spot, p1_score, dice)
  print("P1: ", p1_spot, p1_score)
  if win:
    print(p2_score, dice-1)
  else:
    p2_spot, p2_score, dice, win = player_turn(p2_spot, p2_score, dice)
    print("P2: ", p2_spot, p2_score)
    if win:
      print(p1_score, dice-1)
