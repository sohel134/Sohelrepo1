import random
guess = input('type a number: ')
if guess.isdigit():
  guess = int(guess)
  if guess <= 0:
    print ('please type a number greater than 0 ')
    quit()
else :
  print ('type a number ')
  quit()

random = random.randint(0,guess)
count = 0
while True:
  count += 1
  Make_guess = input('guess karo number ko')
  if Make_guess.isdigit():
    Make_guess = int(Make_guess)
  else:
    print ('numbers me guess karo')
  if Make_guess == random:
    print('u got it')
    break
  if Make_guess > random:
    print (' ur above ')
  else:
    print ('ur below ')
print (f'u got it in {count} guess')
