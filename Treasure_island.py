print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Alpha]
*******************************************************************************''')

print("Welcome to treasure island!")
print("You are now provided with three choices chose wisely\n Turn right, Turn left, Go straight.")
choice = input("Enter your choice (L,R,S)")
choice = choice.lower()

if choice== 's':
    print("You've found a river.\nDo you want to swim?\n")
    swim=input("Enter Y/N:\n")
    swim=swim.lower()
    if swim=='y':
        print("You've been eaten by a crocodile.\n Game over.\n")
    if swim=='n':
        print("Do you want to use the boat and reach the other side.\n")
        boat = input("Enter Y/N\n")
        boat = boat.lower()
        if boat == 'y':
            print("Congratulations!\nYou found the treasure\nYou win!")
        if boat =='n':
            print("Get out of the island you coward.\n")

if choice== 'l':
    print("You've found a car. Do you want or explore or go out?\n")
    car = input("Enter Y/N:\n")
    car = car.lower()
    if car=='y':
        print("While exploring you've found a cave with two ways (left and right).\nWhich way do you want to go?\n")
        way = input("Enter L/R:\n")
        way = way.lower()
        if way == 'l':
            print("You've been eaten by a dragon.\nGame over.\n")
        if way == 'r' :
            print("Congratulations!\nYou've found the treasure.\nYou win!\n")
    if car=='n':
        print("Ok better wait here untill something eats you up.\n DUMBO!\n")
if choice=='r':
    print("You've fallen into ditch.\nGame Over.\n")