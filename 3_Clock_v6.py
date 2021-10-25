import time
from threading import Thread

# sets the variable used in the time keeper function
answer = None
time_to_answer = 0
timer_reset = False
# sets the time keeper function
def time_keeper():
    # Loops the time keeper function while there is no answer
    while answer == None:
        global time_to_answer,timer_reset
        if timer_reset == True:
            time_to_answer = 0
            timer_reset = False
        time.sleep(1)
        time_to_answer += 1


time_keeper_function = Thread(target=time_keeper)
questions_easy = ["question 1-easy", "question 2-easy","question 3-easy"]
time_keeper_function.start()
for i in questions_easy:
    answer = input("test")
    print(time_to_answer)
    if time_to_answer > 15:
        print("answer rejected")
    elif time_to_answer <15:
        print("answer accepted")
    timer_reset = True


