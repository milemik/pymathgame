import random
from functions import yes, user_answer, number_is_pair, is_right

class MathGame:

    def __init__(self):
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
        return random.randint(1, 50) * self.first_number

    def first_question(self):
        right_answer = number_is_pair(self.random_multiply())
        print("Is your new digital a pair number?\n")
        answer = yes(user_answer())
        print(is_right(value=right_answer, answer=answer))

    def run(self):
        self.validate_is_number()
        result = self.random_multiply()
        print(f"Your new number is {result}")
        self.first_question()


if __name__ == '__main__':
    MathGame().run()
