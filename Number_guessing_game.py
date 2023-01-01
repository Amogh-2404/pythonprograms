from art import logo3
import random

def game():
    comp_guess = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100\n")
    level = input("Choose a difficulty level. Type 'easy' or 'hard':\n").lower()
    if level == "easy":
        life = 10
    else:
        life = 5
    while(life>0):
        print(f"You have {life} guesses remaining")
        num = int(input("Guess a number\n"))

        if num == comp_guess:
            print(f"You got it! The answer was {comp_guess}")
            break
        else:
           if (num<comp_guess):
               life = life - 1
               if (life == 0):
                   print(f"You've exceeded the number of guesses.You lose!\nThe number I had in mind was {comp_guess}")
                   break
               print("Too low.\nGuess again.")
               continue
           if (num>comp_guess):
               life = life - 1
               if (life == 0):
                   print(f"You've exceeded the number of guesses.You lose!\nThe number I had in mind was {comp_guess}")
                   break
               print("Too high.\nGuess again.")
               continue




print(logo3)
print("Welcome to the guessing game\n")
game()