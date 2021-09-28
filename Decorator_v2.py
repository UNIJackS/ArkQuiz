def decorator(input_text, num_of_deco, deco_type):
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))
    print(deco_type * num_of_deco + input_text + deco_type * num_of_deco)
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))


decorator("Test_text", 2, "&")
