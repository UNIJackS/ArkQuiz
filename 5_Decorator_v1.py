def decorator(input_text):
    print("*"*4*2+"*"*len(input_text))
    print("*"*4+input_text+"*"*4)
    print("*"*4*2+"*"*len(input_text))


decorator("Test text 1")
decorator("Test text 2")


