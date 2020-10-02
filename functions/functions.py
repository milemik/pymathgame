def number_is_pair(value):
    if value % 2 == 0:
        return True
    return False


def user_answer():
    return input("Your answer is:\n")


def yes(some_answer):
    if some_answer.lower() == 'y':
        return True
    elif some_answer.lower() == 'n':
        return False
    raise ValueError("Please enter valid answer")


def is_right(value, answer):
    if value == answer:
        return "Nice answer. Are you a programmer???"
    return "EEE wrong answer!"


def solve_simple_function(simple_func):
    import re
    numbers = re.findall('[0-9]', simple_func)
    a, b, c = [int(n) for n in numbers]
    if '+' in simple_func:
        x = (c - b)/a
    if '-' in simple_func:
        x = (c + b) / a
    return x


def pythagora_result(a, b):
    return a*a + b*b
