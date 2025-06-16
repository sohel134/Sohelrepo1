import random
import time

OPERATORE = ['+', '-', '*']
MIN = 2
MAX = 12
TOTALP = 5

def sohel():
    right = random.randint(MIN, MAX)
    left = random.randint(MIN, MAX)
    choi = random.choice(OPERATORE)
    exp = f"{left} {choi} {right}"
    an = eval(exp)
    return exp, an

wrn = 0
input('Press Enter to play...')
print('__________________________')
st = time.time()

for i in range(TOTALP):
    exp, an = sohel()
    while True:
        g = input(f'Problem {i+1}: {exp} = ')
        try:
            if int(g) == an:
                break
            else:
                print("Wrong answer, try again.")
                wrn += 1
        except:
            print("Please enter a valid number.")

et = time.time()
total = et - st

print('__________________________')
print('You finished in', round(total, 2), 'seconds')
print('Wrong attempts:', wrn)
