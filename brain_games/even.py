import random
import prompt


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    attempts = 0
    while attempts < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = (input("Your answer:").lower())
        if (answer == "yes" and is_even(number)) or (answer == "no" and not is_even(number)):
            print("Correct!")
            attempts += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes'if is_even(number) else 'no'}'."
                  f"\nLet's try again, {name}!")
    print(f"Congratulations, {name}!")
