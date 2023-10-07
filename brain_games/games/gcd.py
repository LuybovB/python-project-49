#!/usr/bin/env python3
import random
from math import gcd


DESCRIPTION = ('Find the greatest common '
               'divisor of given numbers.')


def run_game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f'{num_1} {num_2}'

    return question, str(gcd(num_1, num_2))
