import random


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    print("Введите 'yes', если число чётное, или 'no', если число нечётное: ")
    attempts = 0
    while attempts < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = (input("Your answer:"))
        if (answer == "yes" and is_even(number)) or (answer == "no" and not is_even(number)):
            print("Correct!")
            attempts += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, !")


if __name__ == "__main__":
    run_game()
