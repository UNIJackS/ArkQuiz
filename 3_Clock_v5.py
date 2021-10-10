from threading import Thread
import time
import os

answer = None


def question_asker():
    global answer
    answer = input("Input something: \n")


def timer():
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
            os._exit(1)


ask_question = Thread(target=question_asker)
start_timer = Thread(target=timer)

ask_question.start()
start_timer.start()

