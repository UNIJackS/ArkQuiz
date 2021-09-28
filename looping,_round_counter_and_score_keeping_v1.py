def answer_checkcer(input_answer, question_num,):
    answers = ["answer 1", "answer 2", "answer 3"]
    if input_answer == answers[question_num]:
        return True
    else:
        return False

import time
from threading import Thread

# sets the answer to none so that the check function
answer = None


# A function that is used to print the time reminders even if an input is asked
def check():
    timer = 0
    while timer < 39 and answer is None:
        time.sleep(1)
        timer += 1
        if answer is not None:
            return
        if timer == 10:
            print("\n20 seconds Left")
        if timer == 20:
            print("\n10 seconds left")
        if timer == 29:
            print("\nTimes up")
        if timer == 38:
            print("\n"*20)

# calls the check function to print time reminders



score = 0
question_num = 0
answers = ["answer 1", "answer 2", "answer 3"]
questions = ["question 1", "question 2", "question 3", ]

for i in questions:
    Thread(target=check).start()
    answer = input(questions[question_num])
    correct = answer_checkcer(answer, question_num)
    if correct:
        print("correct")
    else:
        print("incorrect")
    question_num += 1
    answer = None
