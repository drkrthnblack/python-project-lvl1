from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def determine_question():
    number = randint(0, 255)
    print('Question: {}'.format(number))
    return number


def determine_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'
