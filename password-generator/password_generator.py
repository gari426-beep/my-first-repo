import random
import string

print('=== Secure Password Generator ===')

length = int(input("Enter the desired password length: "))

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

all_characters = letters + digits + special_characters

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)
             
