import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    return name


NAME = welcome_user()


if __name__ == "__main__":
    name = welcome_user()
    print(f"Hello, {name}!")
