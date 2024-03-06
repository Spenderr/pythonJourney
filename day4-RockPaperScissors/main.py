# import random

# rand = random.randint(1,15)

# print(rand)

# rand2 = random.random()

# print((rand2*10/2))

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Choose Rock Paper or Scissors, choose \'0\'for Rock , \'1\' for Paper \'2\' for Scissors\n"))

compChoice = random.randint(0,2)

print("\nYour choice:")
if choice == 0 :
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)


print("\nComputer Chose:")
if compChoice == 0 :
    print(rock)
elif compChoice == 1:
    print(paper)
else:
    print(scissors)


if choice == compChoice :
    print("Tie game ")
elif (choice == 2 and compChoice==0 ) or ( choice == 1 and compChoice == 2):
    print("You loose")
else:
    print("Congrats you won :)))")