import prompt


QUESTIONS_COUNT = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def correct_answer_mode():
    print('Correct!')


def wrong_answer_mode(answer, correct_answer):
    print("'{}' is wrong answer ;(. Correct answer was '{}'."
          .format(answer, correct_answer))


def ending(is_winner, name):
    if is_winner:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


def run_game(game):
    username = welcome_user()
    print(game.RULES)
    is_winner = True
    for attempt in range(QUESTIONS_COUNT):
        question = game.determine_question()
        correct_answer = game.determine_correct_answer(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            correct_answer_mode()
        else:
            is_winner = False
            wrong_answer_mode(answer, correct_answer)
            break
    ending(is_winner, username)
