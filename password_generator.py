import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_amount = int(input("Welcome to password generator\nHow many letters would you like?\n"))
number_amount = int(input("How many numbers would you like?\n"))
symbol_amount = int(input("How many symbols would you like?\n"))

password = ""

for char in range(letter_amount + 1):
  password += random.choice(letters)

for num in range(number_amount + 1):
  password += random.choice(numbers)

for symbol in range(symbol_amount + 1):
  password += random.choice (symbols)

print(password)
