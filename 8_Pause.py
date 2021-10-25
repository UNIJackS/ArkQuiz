import time


print("started")
time.sleep(10)
print("started")
time = 0
while time < 30:
    if time == 10:
        print("now")
    if time == 24:
        print("now")
    if time == 39:
        print("now")
    time.sleep(1)
    time += 1