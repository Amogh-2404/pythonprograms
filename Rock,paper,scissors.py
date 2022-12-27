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

#Write your code below this line 👇
print ("Enter 0 for rock, 1 for paper and 2 for scissors")
choice = int(input())
if choice==0:
    print(rock)
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print(rock)
        print("Draw\n")
    if computer_choice == 1:
        print(paper)
        print("You lose\n")
    if computer_choice == 2:
        print(scissors)
        print("You win\n")
if choice==1:
    print(paper)
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print(rock)
        print("You win\n")
    if computer_choice == 1:
        print(paper)
        print("Draw\n")
    if computer_choice == 2:
        print(scissors)
        print("You lose\n")
if choice==2:
    print(scissors)
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print(rock)
        print("You lose\n")
    if computer_choice == 1:
        print(paper)
        print("You win\n")
    if computer_choice == 2:
        print(scissors)
        print("Draw\n")

