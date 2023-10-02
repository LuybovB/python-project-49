from brain_games.cli import welcome_user
import random


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    number = random.randint(1, 100)
    print(f"Число: {number}")
    answer = input("Введите 'yes', если число чётное, или 'no', если число нечётное: ")
    if (answer == "yes" and is_even(number)) or (answer == "no" and not is_even(number)):
        print("Correct!")
    else:
        print("""'yes' is wrong answer ;(. Correct answer was 'no'.
        Let's try again, Bill!""")


if __name__ == "__main__":
    run_game()
