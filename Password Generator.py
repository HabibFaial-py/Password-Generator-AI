import random
from random import randint

UpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerCase = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "@#$%*?/"

Use_for = UpperCase + LowerCase + numbers + symbols
length_of_password = randint(8,13)
password = ''.join(random.sample(Use_for, length_of_password))

print("Your AI generated Password is", end=": ")
print(password)A