import time
question = "test question 1","yest question 2"
answer = input("The question is {}".format(question[0]))
count_down = 10
timer = 0
print("time starts now")
while timer < 29:
    time.sleep(1)
    timer += 1
    if timer == 30:
        answer = input("The question is {}".format(question[0]))
    if timer == 10:
        print("20 seconds Left")
    if timer == 20:
        print("10 seconds left")
    if timer > 20:
        count_down -= 1
        print(count_down)


