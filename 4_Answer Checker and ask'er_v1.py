answers = ["answer 1", "answer 2", "answer 3"]
questions = ["question 1", "question 2", "question 3", ]
x = 0
score = 0
for i in questions:
    answer = input("The question is {}".format(questions[x]))
    if answer == answers[x]:
        score += 1
        print("Correct")
    else:
        print("Almost the answer was {}".format(answers[x]))
    x += 1
    if score == 1:
        print("you have {} point".format(score))
    else:
        print("you have {} points".format(score))

