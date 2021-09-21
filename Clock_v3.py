import time
from threading import Thread

answer = None


def check():
    time.sleep(2)
    if answer is not None:
        return
    timer = 0
    while timer < 29:
        time.sleep(1)
        timer += 1

        if timer == 10 and answer is None:
            print("\n20 seconds Left")
        if timer == 20 and answer is None:
            print("\n10 seconds left")


Thread(target=check).start()

answer = input("Input something: ")

if answer == "nine":
    print("correct")
