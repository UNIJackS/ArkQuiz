questions_easy = ["question 1-easy", "question 2-easy"]
answers_easy = ["answer 1-easy", "answer 2-easy"]
questions_normal = ["question 1-normal", "question 2-normal"]
answers_normal = ["answer 1-normal", "answer 2-normal"]
questions_hard = ["question 1-hard", "question 2-hard"]
answers_hard = ["answer 1-hard", "answer 2-hard"]


question = input("What diffacuty would you like to play at ?").strip()
if question == "easy":
    print(questions_easy)
    print(answers_easy)
elif question == "normal":
    print(questions_normal)
    print(answers_normal)
elif question == "hard":
    print(questions_hard)
    print(answers_hard)
else:
    print("Pleas enter easy,normal or hard")
    print()



