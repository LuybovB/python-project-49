#!/usr/bin/env python3
from random import randint


DESCRIPTION = ('What number is missing'
               'in the progression?')


def run_game():
    start = randint(1, 100)
    difference = randint(2, 5)
    length = randint(4, 10)
    progression = list(range(start, start + difference * length, difference))
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = " ".join(map(str, progression))
    return question, str(correct_answer)
