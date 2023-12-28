

import random

print('Welcome To Your Password Generator')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input('Amount of Passwords to generate: '))

length = int(input ('Input Your Password Length: '))

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)