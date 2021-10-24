import time
from threading import Thread

answer = None


def timer():
    time.sleep(2)
    if answer is not None:
        return
    count_down = 10
    timer = 0
    while timer < 29:
        time.sleep(1)
        timer += 1

        if timer == 10 and answer is None:
            print("20 seconds Left")
        if timer == 20 and answer is None:
            print("10 seconds left")
        if timer > 20 and answer is None:
            count_down -= 1
            print("{} seconds left".format(count_down))

Thread(target=timer).start()

answer = input("Input something: ")

if answer == "nine":
    print("correct")

