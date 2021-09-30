import random


def randomizer():
    question_num = random.randint(0,1)
    return[questions[question_num],answers[question_num]]


random_question_answer = randomizer()
print(random_question_answer[0])
print(random_question_answer[1])
