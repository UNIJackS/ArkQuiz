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
            # The invalid counter counts how many invalid answers have been entered if this reaches 5 then it prints a..
            # -different error message It does this with 2 an if statement which is just bellow the variable
            invalid_counter += 1
            if invalid_counter != 5:
                print("Please enter Yes or No ")
            else:
                print("yes or no are the only valid answers, you must enter yes or no")


# instructions function. It will print the instructions when called
def instructions():
    # print statements that print the instructions
    print(" ")
    print("Welcome to the Quiz")
    print("You will have 30 seconds to answer each question")
    print("Answers will only be accepted in English")
    print("Capitols and spaces are not necessary but if included will not void your answer")
    print("Enjoy the quiz")
    print(" ")


# code for the answer checker function. This compares 2 strings and a time the outputs a ture or false
def answer_checker(input_answer, correct_answer, time_limit):
    # an if statement that compares the input answer to the answer and to the time limit to the time to answer
    if input_answer == correct_answer and time_to_answer < time_limit:
        return ["Congratulations that is correct", True]
    elif input_answer == correct_answer and time_to_answer > time_limit:
        return ["That is correct however you ran out of time", False]
    else:
        return ["Sorry that is incorrect. The answer was {}".format(correct_answer), False]


# randomizer function that returns a random question and its answer from the questions and answers lists.
def randomizer():
    while not valid_num:
        # sets a variable (num_of_questions) as the amount of questions in the variable questions - 1
        num_of_questions = len(questions) - 1
        # sets the question number randomly from 0 to the amount of question's in questions - 1
        question_num = random.randint(0, num_of_questions)

        # Checks if the random number selected is in the list of numbers that have already been used
        if question_num not in numbers_used:
            # adds the number selected to the used numbers list so that it can not be used again
            numbers_used.append(question_num)
            # returns the randomly selected question and answer
            return [questions[question_num], answers[question_num]]


# Code for the difficulty selector that when called asks the user which difficulty they would like to play on then
def difficulty_selector():
    valid = False
    while not valid:
        # An input statement that asks the user what difficulty they want to play at
        difficultly_input = input("\nWhat difficulty would you like to play at ?\n :").strip()
        # An If statement that checks if the user inputted either easy,normal or hard and if not prints an error message
        if difficultly_input == "easy":
            return [questions_easy, answers_easy]
        elif difficultly_input == "normal":
            return [questions_normal, answers_normal]
        elif difficultly_input == "hard":
            return [questions_hard, answers_hard]
        else:
            print("Pleas enter easy,normal or hard")
            print()


# sets the time keeper function
def time_keeper():
    # Loops the time keeper function while there is no answer
    while answer is None:
        global time_to_answer, timer_reset
        if timer_reset:
            time_to_answer = 0
            timer_reset = False
        time.sleep(1)
        time_to_answer += 1


# A function that decorates text that is imputed when it is called
def decorator(input_text, num_of_deco, deco_type):
    # code that sets a variable in this case line1 as the number of the chosen symbol twice plus 1 for every character in
    # the text imputed
    line1 = (deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # code that sets a variable in this case line2 as the number of the chosen symbols on either side of the input text
    # and the input text
    line2 = (deco_type * num_of_deco + input_text + deco_type * num_of_deco)
    # code that sets a variable in this case line3 as the number of the chosen symbol twice plus 1 for every character
    # in the text imputed
    line3 = (deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # returns the 3 lines in a list with \n to put them on separate lines when printed
    return "{}\n{}\n{}".format(line1,line2,line3)


# Main program

# question and answer bank with all the questions and answers for each difficulty
questions_easy = ["What is the name of the 2nd story DLC ?",
                  "What is the name of the bay located in the north west corner of ragnarok ?",
                  "What is the name of the giant carnivore that spawns in the highlands of ragnarok ?",
                  "In which biome is the red obelisk located next to on ragnarok ?",
                  "what type/element of wyvern applies torpo with its breath weapon ?",
                  "Which meat is most effective for taming carnivores ?",
                  "Which berry is most effective for taming herbivores ?",
                  "How many metal ingots are required for an industrial forge ?",
                  "Which ark has malfunctioned causing searing heat ?",
                  "What is the full name for the dino that can run for short bursts after being in contact with water ?"]
answers_easy = ["aberration", "viking Bay", "giganotosaurus", "redwoods", "poison", "mutton", "mejoberry", "2500",
                "scorched earth", "spinosaurus"]
questions_normal = ["What is the full name of the dino shortened to Trike ?",
                    " What is the weapon used to fire darts called ?",
                    " what resources are castoroides dams raided for ?",
                    " What is the full name for the dino that is commonly used for metal farming ?",
                    "What is the full name for the dino that is commonly used for stone farming ?",
                    "What is the full name of the dino that can have a platform saddle and can fly ?",
                    " what is the highest quality of equipment available ?",
                    " How much metal ore is required to craft 1 metal ingot in a forge",
                    " How many creatures start their name with dire ?",
                    " Which creature can protect you from bees if you ride it ?",
                    "Do triceratops get buff against carnivores larger than it ?"]
answers_normal = ["triceratops", "longneck rifle", "cementing paste", "ankylosaurus", "doedicurus", "Quetzal",
                  "ascendant", "2", "2", "dire bear", "yes"]
questions_hard = ["What is the name of the main antagonist ?", "how many difficulties are there for each boss ?",
                  "What is the name of the hardest boss difficulty ?", " Does ragnarok have explorer notes ?",
                  "does genesis part 2 have explorer notes ?", "At what level can you make Tranquilizer Dart’s ?",
                  "how many metal ingots does a Tranquilizer Dart cost in total (including the rifle ammo) ?",
                  "can wyverns carry 2 creatures at once ?", "How many hexagons do 20 pieces of crystal cost ?",
                  "does the chem bench require a generator to power it ?"]
answers_hard = ["rockwell", "3", "alpha", "no", "yes", "62", "3", "no", "230", "yes"]

# sets the initial values for the main program
answer = None
timer_reset = False
score = 0

# asks the user if they would like to see the instructions then calls the yes no checker to determine there answer
show_instructions = yes_no_checker("Would you like to see the instructions ?\n :")

valid_num = False
numbers_used = []
# checks if the user entered yes and if so it calls the instructions function
if show_instructions == "yes":
    instructions()

# calls the difficulty selector function then converts its answer into the question and answer variables
questions_and_answers = difficulty_selector()
questions = questions_and_answers[0]
answers = questions_and_answers[1]

# sets a separate variable as the number of questions because the num of questions variable gets changed and i need the
# original number for the final print statement
unmodified_num_of_questions = len(questions)
num_of_questions_for_loop = len(questions)

# starts the time keeper function a separate thread so it can run parallel with the main program. This is so it is not
# interrupted by the input statements
Thread(target=time_keeper).start()

# The main loop that loops the functions that are responsible for time keeping, question asking, score keeping etc
while num_of_questions_for_loop > 0:
    answer = None
    time_to_answer = 0
    # calls the random question and answer generator and then sets the list of the 2 as a random_question_and_answer
    random_question_and_answer = randomizer()
    # sets the answer variable as an input with the randomly generated question which is then decorated by the decorator
    answer = input("\n{} \n :".format(random_question_and_answer[0]))
    # sets the global varable of timer_reset as true which resets the time in the time keeper function
    timer_reset = True
    # compares the answer inputted before to the matching randomly selected answer and the time to answer from the
    # time keeper function to the time limit of 15 seconds
    correct = answer_checker(answer, random_question_and_answer[1], 15)
    # checks if the second variable in the correct list is True and if so it then it prints the second correct variable
    # which is decorated by the decorator function
    if correct[1]:
        print(decorator(correct[0], 2, "!"))
        score += 1
    # prints the second correct value if the first correct value is not True which is also decorated by the decorator
    # function
    else:
        print(decorator(correct[0], 2, "?"))
    # takes one off the num_of_questions_for_loop varable this allows the loop to stop and not loop forever
    num_of_questions_for_loop -= 1
# prints a thank you for playing and some stats about how well you did
print("\nThank you for playing this is the end of the quiz your scored {} out of {} or {}%".format(score,
                                                                                                   unmodified_num_of_questions,
                                                                                                   100 / unmodified_num_of_questions * score))
