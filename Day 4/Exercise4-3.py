import random
number = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose =[Rock,Paper,Scissors]
userChoose = choose[number]
print(userChoose)
print('Computer Choose : ')
computerChoose = choose[random.randint(0,1)]
print(computerChoose)

if userChoose == computerChoose:
    print('Both Wins The Game')
elif userChoose == choose[0]  and computerChoose == choose[1] or userChoose == choose[1] and computerChoose == choose[2] or userChoose == choose[2] and computerChoose == choose[0]:
    print('you Lose') 
elif userChoose == choose[1] and computerChoose == choose[0] or userChoose == choose[2] and computerChoose == choose[1] or userChoose == choose[0] and computerChoose == choose[2]:
    print('you Win')
else:
    print('invalid Number')