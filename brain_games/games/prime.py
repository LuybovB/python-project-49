#!/usr/bin/env python3
from random import randint


DESCRIPTION = ('Answer "yes" if given number '
               'is prime. Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        else:
            return True


def run_game():
    num = randint(0, 100)
    question = f'{num}'
    if is_prime(num):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
