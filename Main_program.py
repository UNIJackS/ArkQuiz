import random
import time
from threading import Thread


def yes_no_checker(question):
    # loops the if statement until a valid answer is entered
    invalid_counter = 0
    loop = True
    while loop:
        # asks the user yes or no this is just for testing then stores it as yes_or_no. It also strip's and lowers the variable
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
    print("You will have 30 seconds to answer each question")
    print("Answers will only be accepted in English")
    print("Capitols and spaces are not necessary but if included will not void your answer")
    print("Enjoy the quiz")
    print(" ")


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
            print("\n" * 20)


def answer_checkcer(input_answer, answer):
    if input_answer == answer:
        return True
    else:
        return False


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


questions_easy = ["question 1-easy", "question 2-easy"]
answers_easy = ["answer 1-easy", "answer 2-easy"]
questions_normal = ["question 1-normal", "question 2-normal"]
answers_normal = ["answer 1-normal", "answer 2-normal"]
questions_hard = ["question 1-hard", "question 2-hard"]
answers_hard = ["answer 1-hard", "answer 2-hard"]

score = 0
# Main program
show_instructions = yes_no_checker("Would you like to see the instructions ?")
if show_instructions == "yes":
    instructions()

questions_answers = difficulty_selector()
questions = questions_answers[0]
answers = questions_answers[1]

while len(questions) > 0:
    # calls the randomizer function
    random_question_answer = randomizer()
    Thread(target=check).start()
    while answer =
        answer = input("The questions is {}".format(random_question_answer[0]))
    answer_checkcer(answer,random_question_answer[1])
    if answer_checkcer == True:
        score += 1
        print(score)
    questions.remove(random_question_answer[0])
    answers.remove(random_question_answer[1])

print("out of questions")