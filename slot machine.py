import random
MAX_LINE = 4
MAX_BET = 150
MIN_BET = 1
ROW = 3
COL = 3
symbol_count = {
  "A":2,
  "B":4,
  "C":6,
  "D":8
  
}

def get_slot_machine_spin(row,cols,symbol):
  all_symbol = []
  for sym ,symbol_count in symbol.items():
    for _ in range(symbol_count):
      all_symbol.append(sym)
  
  columns = []
  for _ in range(cols):
    column = []
    current_symbol = all_symbol[:]
    for _ in range(row):
      value = random.choice(current_symbol)
      current_symbol.remove(value)
      column.append(value)
    columns.append(column)
  return columns 
  
  
def deposit():
    while True:
        money = input('kitna deposit kare ga: ')
        if money.isdigit():
            money = int(money)
            if money > 0:
                return money
            else:
                print('Paise 0 se zyada hone chahiye.')
        else:
            print('Invalid number, sirf number daalo.')

def get_number_of_line():
    while True:
        line = input('kitna line me bet karega: (1-4) ')
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                return line
            else:
                print(f'Sirf 1 se {MAX_LINE} ke beech line choose karo.')
        else:
            print('Invalid number, sirf number daalo.')

def get_bet():
  while True:
    bet = input('kitna bet karoge each line me')
    if bet.isdigit:
      bet=int(bet)
      if MIN_BET <= bet <= MAX_BET:
        return bet
      else:
          print (f' bet must be between {MIN_BET} - {MAX_BET} ')
    else:
      print ('enter invalid number ')
      
  
def main():
  money = deposit()
  lines = get_number_of_line()
  while True:
    bets = get_bet()
    total_bet = bets * lines
    if total_bet > money:
      print (f'you are betting more than u have u have {money} ')
    else:
      break
  print(f'your are betting {bets} on {lines} line and your total bet is {total_bet} ')

main()