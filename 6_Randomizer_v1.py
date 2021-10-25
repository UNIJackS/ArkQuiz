import random

questions = ["question 1", "question 2"]
answers = ["answer 1", "answer 2"]


def randomizer():
    question_num = random.randint(0,1)
    return[questions[question_num],answers[question_num]]


random_question_answer = randomizer()
print(random_question_answer[0])
print(random_question_answer[1])


