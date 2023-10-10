#!/usr/bin/env python3
import random
from math import gcd


DESCRIPTION = ('What number is missing'
               'in the progression?')


def run_game():
    length = random.randint(4, 10)
    hidden_position = random.randint(0, length - 1)
    difference = random.randint(1, 10)
    question = []
    hidden_number = None

    for i in range(length):
        if i == hidden_position:
            question.append("..")
            hidden_number = (i + 1) * difference
        else:
            number = random.randint(1, 100)
            question.append(number)

    return question, hidden_number
