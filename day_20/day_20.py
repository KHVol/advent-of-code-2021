# 20.1
from copy import deepcopy
def pixels_to_decimal(pixel_str: str) -> int:
  bin_str = pixel_str.replace('#', '1').replace('.', '0')
  return int(bin_str, 2)

def lit_pixels(image: list) -> int:
  total = 0
  for i in range(len(image)):
    for j in range(len(image)):
      if image[i][j] == '#':
        total += 1
  return total

def print_image(image: list):
  for i in range(len(image)):
    img_line = ''
    for j in range(len(image[i])):
      img_line += image[i][j]
    print(img_line)
  print("\n")

def get_surrounding_pixels(image: list, x: int, y: int) -> str:
  top_3 = image[x-1][y-1] + image[x-1][y] + image[x-1][y+1]
  mid_3 = image[x][y-1] + image[x][y] + image[x][y+1]
  low_3 = image[x+1][y-1] + image[x+1][y] + image[x+1][y+1]
  return top_3 + mid_3 + low_3

def enhance_image(img, size, alg) -> list:
  new_img = deepcopy(img)
  for x in range(1, size-1):
    for y in range(1, size-1):
      index = pixels_to_decimal(get_surrounding_pixels(img, x, y))
      if alg[index] == '#':
        new_img[x][y] = '#'
      else:
        new_img[x][y] = '.'
  return new_img

def add_padding(img: list, padding_char) -> list:
  size = len(img) + 4
  for row in img:
    # Need to add to the beginning of each row
    row.insert(0, padding_char)
    row.insert(0, padding_char)
    # Need to add to the end of each row
    row.extend([padding_char] * 2)
  img.insert(0, [padding_char] * size)
  img.insert(0, [padding_char] * size)
  img.extend([[padding_char] * size])
  img.extend([[padding_char] * size])
  return img

def remove_padding(img: list) -> list:
  size = len(img) - 2
  img.pop(0)
  img.pop(size)
  for row in img:
    row.pop(0)
    row.pop(size)
  return img

with open('input.txt') as f:
  lines = f.read().splitlines()

# Setup image enhancement algorithm
image_alg = lines.pop(0)
lines.pop(0)
img_size = len(lines[0])

# Setup image
# The image can only grow one space at a time, so just add two '.' in each direction.
image = []
for line in lines:
  chars = []
  for i in range(len(line)):
    chars.append(line[i])
  image.append(chars)

# image = add_padding(image, '.')
# print_image(image)

# new_image = enhance_image(image, len(image), image_alg)
# new_image = remove_padding(new_image)
# new_image = add_padding(new_image, image_alg[0])
# print_image(new_image)

# newer_image = enhance_image(new_image, len(new_image), image_alg)
# newer_image = remove_padding(newer_image)
# print_image(newer_image)

# print(lit_pixels(newer_image))

# 20.2
image = add_padding(image, '.')
for i in range(50):
  image = enhance_image(image, len(image), image_alg)
  padding = image_alg[pixels_to_decimal(image[0][0]*9)]
  image = remove_padding(image)
  print_image(image)
  # It should be 0,0 lit * 9 passed into
  image = add_padding(image, padding)

image = remove_padding(image)
print(lit_pixels(image))
