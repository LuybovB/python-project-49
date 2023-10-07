import random

DESCRIPTION = ('Answer "yes" if the '
               'number is even, otherwise answer "no".')


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    number = random.randint(1, 100)
    correct_answer = ''

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
