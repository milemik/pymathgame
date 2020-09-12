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
