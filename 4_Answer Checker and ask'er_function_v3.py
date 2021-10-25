

# code for the answer checker function. This compares 2 strings and a time the outputs a ture or false
def answer_checkcer(input_answer, answer, time_limit):
    # an if statement that compares the input answer to the answer and to the time limit to the time to answer
    if input_answer == answer and time_to_answer < time_limit:
        return ["Congratulations that is correct", True]
    elif input_answer == answer and time_to_answer > time_limit:
        return ["That is correct however you ran out of time", False]
    else:
        return ["Sorry that is incorrect", False]


# sets the variable's so that the answer checker function can function
score = 0
question_num = 0
answers = ["answer 1", "answer 2", "answer 3", "answer 4"]
questions = ["question 1", "question 2", "question 3", "question 4"]

# a loop that loops for as many questions
for i in questions:
    time_to_answer = int(input("how long did it take to answer in seconds (this is just to test)"))
    answer = input(questions[question_num])
    correct = answer_checkcer(answer, answers[question_num], 15)
    if correct[1]:
        print(correct[0])
    else:
        print(correct[0])
    question_num += 1

