import random
def comparar(choice1,choice2):
  if choice1 == choice2:
    return 'tie'
  elif choice1 == 'paper':
    if choice2 == 'rock':
      return 'you win'
    elif choice2 == 'scissors':
      return 'you lose'
  elif choice1 == 'rock':
    if choice2 == 'scissors':
      return 'you win'
    elif choice2 == 'paper':
      return 'you lose'
  elif choice1 == 'scissors':
    if choice2 == 'paper':
      return 'you win'
    elif choice2 == 'rock':
      return 'you lose'

Usrchoice = raw_input('>> ')

computerChoice = random.randint(1,3)
if computerChoice == 1:
  computerChoice = 'paper'
elif computerChoice == 2:
  computerChoice = 'rock'
elif computerChoice == 3:
  computerChoice = 'scissors'
print comparar(Usrchoice,computerChoice)
