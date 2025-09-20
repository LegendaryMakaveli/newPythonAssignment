import random

positive_responses = [
    "Very good!",
    "Excellent!",
    "Nice work!",
    "Keep up the good work!"
]

negative_responses = [
    "No. Please try again.",
    "Wrong. Try once more.",
    "Don’t give up!",
    "No. Keep trying."
]


def ask_question():
    firstNumber = random.randint(1,9)
    secondNumber = random.randint(1, 9)
    answer = int(input(f"what is {firstNumber} times {secondNumber}? "))

    if answer == firstNumber * secondNumber:
        print(random.choice(positive_responses))
    else:
        print(random.choice(negative_responses))

ask_question()
