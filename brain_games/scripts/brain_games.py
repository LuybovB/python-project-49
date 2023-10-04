#!/usr/bin/env python3.
from .brain_even import run_game
from brain_games.cli import welcome_user


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    print("Welcome to the Brain Games!")
    run_game()


if __name__ == "__main__":
    main()
    welcome_user()
    run_game()
