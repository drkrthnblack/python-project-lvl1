from random import randint, choice
from operator import add, sub, mul


RULES = 'What is the result of the expression?'


def determine_question():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    operations = {'+': add, '-': sub, '*': mul}
    selected_operation = choice(('+', '-', '*'))
    print('Question: {} {} {}'.format(number_1, selected_operation, number_2))
    return number_1, operations[selected_operation], number_2


def determine_correct_answer(question):
    number_1, operation, number_2 = question
    return str(operation(number_1, number_2))
