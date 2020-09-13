import random
from functions.functions import yes, user_answer, number_is_pair, is_right, solve_simple_function
from common.common import start_image

class MathGame:

    def __init__(self):
        start_image()
        self.first_number = input("Enter some random number:\n")

    def validate_is_number(self):
        while True:
            if self.first_number.isdigit():
                self.first_number = int(self.first_number)
                break
            self.first_number = input("Enter some random number:\n")
            print("Please enter a valid number")

    def random_multiply(self):
        """Get some random number between 1 and 50 and multiply it by our number"""
        self.random_num = random.randint(1, 50) * self.first_number
        return self.random_num

    def first_question(self):
        right_answer = number_is_pair(self.random_num)
        print("Is your new digital a pair number?\n")
        answer = yes(user_answer())
        print(is_right(value=right_answer, answer=answer))

    def second_question(self):
        question_function = f"9x + 4 = 1"
        print(f"Solve simple function: {question_function}\nFind value x!!!")
        result = round(solve_simple_function(question_function), 2)
        users_answer = float(input("Enter value of x:\n"))
        print(is_right(result, users_answer))


    def run(self):
        self.validate_is_number()
        result = self.random_multiply()
        print(f"Your new number is {result}")
        self.first_question()
        self.second_question()


if __name__ == '__main__':
    MathGame().run()
