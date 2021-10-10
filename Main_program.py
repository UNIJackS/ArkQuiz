import random
import time
from threading import Thread


def yes_no_checker(question):
    # loops the if statement until a valid answer is entered
    invalid_counter = 0
    loop = True
    while loop:
        # asks the user yes or no this is just for testing then stores it as yes_or_no. It also strip's and lowers
        # the variable
        yes_or_no = input(question).strip().lower()
        # an if statement that checks if they entered yes or y or no or n then prints what they entered as yes or no
        if yes_or_no == "yes" or yes_or_no == "y":
            return "yes"

        elif yes_or_no == "no" or yes_or_no == "n":
            return "no"

        # The else statement outputs an error asking the user to pleas enter yes or no
        else:
            # The invalid counter counts how many invalid answers have been entered if this reaches 5 then it prints a...
            # -different error message It does this with 2 an if statement which is just bellow the variable
            invalid_counter += 1
            if invalid_counter != 5:
                print("Please enter Yes or No ")
            else:
                print("yes or no are the only valid answers, you must enter yes or no")


def instructions():
    print(" ")
    print("Welcome to the Quiz")
    print("You will have 15 seconds to answer each question")
    print("Answers will only be accepted in English")
    print("Capitols and spaces are not necessary but if included will not void your answer")
    print("Enjoy the quiz")
    print(" ")


def answer_checker(input_answer, answer, time_limit):
    if input_answer == answer and time_to_answer < time_limit:
        return ["Congratulations that is correct", True]
    elif input_answer == answer and time_to_answer > time_limit:
        return ["That is correct however you ran out of time", False]
    else:
        return ["Sorry that is incorrect", False]


# A function that decorates text that is imputed when it is called
def decorator(input_text, num_of_deco, deco_type):
    # A print statement that prints the number of the chosen symbol twice plus 1 for every character in the text imputed
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # A print statement that prints the number of the chosen symbols on either side of the input text and the input text
    print(deco_type * num_of_deco + input_text + deco_type * num_of_deco)
    # A print statement that prints the number of the chosen symbol twice plus 1 for every character in the text imputed
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))


# randomizer function that returns a random question and its answer from the questions and answers lists.
def randomizer():
    # sets a variable (num_of_questions) as the amount of questions in the variable questions - 1
    num_of_questions = len(questions) - 1
    # sets the question number randomly from 0 to the amount of question's in questions - 1
    question_num = random.randint(0, num_of_questions)

    # returns the random question and answer that as picked
    return [questions[question_num], answers[question_num]]


def difficulty_selector():
    valid = False
    while not valid:
        question = input("What difficulty would you like to play at easy, normal or hard ?").strip()
        if question == "easy":
            return [questions_easy, answers_easy]
        elif question == "normal":
            return [questions_normal, answers_normal]
        elif question == "hard":
            return [questions_hard, answers_hard]
        else:
            print("Pleas enter easy,normal or hard")
            print()


def time_keeper():
    while answer is None:
        global time_to_answer, timer_reset
        if timer_reset:
            time_to_answer = 0
            timer_reset = False
        time.sleep(1)
        time_to_answer += 1


# Main program

# question and answer bank with all the questions and answers for each difficulty
questions_easy = ["question 1-easy", "question 2-easy"]
answers_easy = ["answer 1-easy", "answer 2-easy"]
questions_normal = ["question 1-normal", "question 2-normal"]
answers_normal = ["answer 1-normal", "answer 2-normal"]
questions_hard = ["question 1-hard", "question 2-hard"]
answers_hard = ["answer 1-hard", "answer 2-hard"]

# asks the user if they would like to see the instructions then calls the yes no checker to determine there answer
show_instructions = yes_no_checker("Would you like to see the instructions ?")

# checks if the user entered yes and if so it calls the instructions function
if show_instructions == "yes":
    instructions()

# calls the difficulty selector function then converts its answer into the question and answer variables
questions_and_answers = difficulty_selector()
questions = questions_and_answers[0]
answers = questions_and_answers[1]

# sets the time keeper function
time_keeper_function = Thread(target=time_keeper)

# sets a separate variable as the number of questions because the num of questions variable gets changed and i need the
# original number for the final print statement
unmodified_num_of_questions = len(questions)

answer = None
timer_reset = False
score = 0
time_keeper_function.start()
for i in questions_hard:
    answer = None
    time_to_answer = 0
    random_question_and_answer = randomizer()
    answer = input("\nThe question is {} \n :".format(random_question_and_answer[0]))
    timer_reset = True
    correct = answer_checker(answer, random_question_and_answer[1], 15)
    if correct[1]:
        print(correct[0])
        score += 1
    else:
        print(correct[0])
    questions.remove(random_question_and_answer[0])
    answers.remove(random_question_and_answer[1])

print("Thank you for playing this is the end of the quiz your scored {} out of {} or {}%".format(score,
                                                                                                 unmodified_num_of_questions,
                                                                                                 100 / unmodified_num_of_questions * score))
