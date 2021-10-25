
def answer_checkcer(input_answer, answer):
    if input_answer == answer:
        return True
    else:
        return False


score = 0
question_num = 0
answers = ["answer 1", "answer 2", "answer 3"]
questions = ["question 1", "question 2", "question 3", ]

for i in questions:
    answer = input(questions[question_num])
    correct = answer_checkcer(answer, question_num)
    if correct:
        print("correct")
    else:
        print("incorrect")
    question_num += 1

