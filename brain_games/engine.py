import prompt

ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.DESCRIPTION}')

    for _ in range(ROUNDS):
        question, correct_answer = game.run_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
