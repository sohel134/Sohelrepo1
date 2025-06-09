import random
COLOR_CODE = ['R','G','B','Y','W','O']
TRY = 8
CODE_LENGTH = 4
def generate_code():
  code = []
  for _ in range(CODE_LENGTH):
    color = random.choice(COLOR_CODE)
    code.append(color)
  return code
   
def guess_code():
  while True:
    guess = list(input("Guess 4 colors (e.g. RGBY or R,G,B,Y): ").upper().replace(',', ''))
    if len(guess) != CODE_LENGTH:
      print(f'u must be {CODE_LENGTH} Color ')
      continue
    for Color in guess:
      if Color not in COLOR_CODE:
        print(f"invalid colors {Color} try again ")
        break
    else:
      break
  return guess
  
def check_code(guess,real_code):
  color_counts = {}
  correct_pos = 0
  incorrect_pos = 0
  for color in real_code:
    if color not in color_counts:
      color_counts[color] = 0
    color_counts[color] += 1
  for guess_color,real_color in zip(guess,real_code):
    if guess_color == real_color:
      correct_pos += 1
      color_counts[guess_color] -= 1
  
  for guess_color,real_color in zip(guess ,real_code):
    if guess_color in color_counts and color_counts[guess_color] > 0:
      incorrect_pos += 1 
      color_counts[guess_color] -= 1
      
  return correct_pos,incorrect_pos
  
def game():
  print(f"welcome to mastermind game u have {TRY} to guess the code")
  print("u have this valid option ",*COLOR_CODE)
  code = generate_code()
  for attempt in range(1,TRY + 1):
    guess = guess_code()
    correct_pos,incorrect_pos = check_code(guess,code)
    if correct_pos == CODE_LENGTH:
      print (f"u guess in {attempt} try")
      break
    print(f"correct_pos {correct_pos} incorrect_pos {incorrect_pos} ")
  else:
    print(f"u ran out of try the code wad ", *code)
    
    
if __name__ == "__main__":
  game()