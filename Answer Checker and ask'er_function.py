
def answer_chcekcer(question_num,answer):
    answers = ["answer 1", "answer 2", "answer 3"]
    score = 0
    if answer == answers[question_num]:
        return "Correct"
    else:
        return ("Almost the answer was {}".format(answers[question_num]))


questions = ["question 1", "question 2", "question 3", ]
question_num_1 = 0
for i in questions:
    answer = input("The question is {}".format(questions[question_num_1]))
    correct = answer_chcekcer(question_num_1,answer)
    question_num_1 += 1



if score == 1:
    print("you have {} point".format(score))
else:
   print("you have {} points".format(score))
