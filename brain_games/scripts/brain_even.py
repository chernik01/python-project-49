#!/usr/bin/env python3
import prompt
import random


def is_even():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    flag = True
    i = 1

    while i <= 3:
        number = random.randint(1, 100)
        print('Question:', number)
        ui = prompt.string('Your answer: ')
        if number % 2 == 0 and ui == 'yes':
            print('Correct!')
            i += 1
        elif number % 2 != 0 and ui == 'no':
            print('Correct!')
            i += 1
        else:
            if number % 2 == 0:
                right_ui = 'yes'
            else:
                right_ui = 'no'
            print(f"'{ui}'is wrong answer;(. Correct answer was '{right_ui}'")
            print(f"Let's try again, {name}!")
            flag = False
            break
    if flag is True:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    is_even()


if __name__ == '__main__':
    main()
