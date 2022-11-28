import string
import random
numbers = string.digits
alphabet = string.ascii_letters
special_char = string.punctuation
all_characters = numbers + alphabet + special_char

size  = int(input('Please enter prefered length of password:)'))
password = []
for i in range(size):
    password += random.choice(all_characters)


print(''.join(password))

#make use of secret module
