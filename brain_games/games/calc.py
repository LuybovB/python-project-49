import prompt
import random

DESCRIPTION = ('Answer "yes" if the '
               'number is even, otherwise answer "no".')


def run_game():
    operations = ['+', '-', '*']
    operand = random.choice(operations)
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f'{num_1} {operand} {num_2}'
    if operand == '+':
        correct_answer = num_1 + num_2
    elif operand == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
