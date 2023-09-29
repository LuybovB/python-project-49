#!/usr/bin/env python3.
import prompt
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
    welcome_user()

