#!/usr/bin/env python3
"""Number guessing game"""

import random

separator = '--------------------------------'

print(separator)
print('       GUESS THE NUMBER')
print(separator)

number = random.randint(0, 100)

guess_text = input('Guess a number between 0 and 100: ')
guess = int(guess_text)

while guess != number:
    if guess < number:
        print('Sorry, your guess of {} was too low.'.format(guess))
    elif guess > number:
        print('Sorry, your guess of {} was too high.'.format(guess))

    guess_text = input('Guess again: ')
    guess = int(guess_text)

print('Nailed it! You win!')
