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

loop_1 = 0
while loop_1 < 10:
    test_variable = yes_no_checker("yes or no ? ")
    print(test_variable)
    loop_1 += 1

