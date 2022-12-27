#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Easycode
# for x in range(0 , nr_letters):
#     i = random.randint(0,25)
#     print(letters[i],end="")
#
# for x in range(0 , nr_numbers):
#     i = random.randint(0,9)
#     print(numbers[i],end="")
#
# for x in range(0 , nr_symbols):
#     i = random.randint(0,8)
#     print(symbols[i],end="")

# Mastercode
# Add everything into a list first
password_list = []

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

# Change the order of items in a list. Use the random.shuffle function.
random.shuffle(password_list)
password = ""
for x in password_list:
    password += x

print(f"Your suggested strong password is:\n{password}")


