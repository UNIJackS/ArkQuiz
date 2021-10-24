import time
from threading import Thread

# sets the answer to none so that the check function
answer = None


# A function that is used to print the time reminders even if an input is asked
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
            print("\n"*20)

# calls the check function to print time reminders
Thread(target=timer).start()

# asks the user a question then waits for a response
answer = input("Input something: ")

if answer == "nine":
    print("correct")

