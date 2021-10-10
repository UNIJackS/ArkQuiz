import time
from threading import Thread

answer = None
time_to_answer = 0
timer_reset = False

def time_keeper():
    while answer == None:
        global time_to_answer,timer_reset
        if timer_reset == True:
            time_to_answer = 0
            timer_reset = False
        time.sleep(1)
        time_to_answer += 1


time_keeper_function = Thread(target=time_keeper)
questions_easy = ["question 1-easy", "question 2-easy"]
time_keeper_function.start()
for i in questions_easy:
    answer = input("test")
    print(time_to_answer)
    timer_reset = True


