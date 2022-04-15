import prompt
from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'



def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def determine_question():
    number = randint(0, 255)
    print('Question: {}'.format(number))
    return number


def determine_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def correct_answer_mode():
    print('Correct!')


def wrong_answer_mode(answer, correct_answer):
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))


def ending(is_winner, name):
    if is_winner:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


questions_count = 3


def run_game():
    username = welcome_user()
    print(RULES)
    is_winner = True
    for attempt in range(questions_count):
        question = determine_question()
        correct_answer = determine_correct_answer(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            correct_answer_mode()
        else:
            is_winner = False
            wrong_answer_mode(answer, correct_answer)
            break
    ending(is_winner, username)

#run_game()