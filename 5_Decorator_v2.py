# A function that decorates text that is imputed when it is called
def decorator(input_text, num_of_deco, deco_type):
    # A print statement that prints the number of the chosen symbol twice plus 1 for every character in the text imputed
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # A print statement that prints the number of the chosen symbols on either side of the input text and the input text
    print(deco_type * num_of_deco + input_text + deco_type * num_of_deco)
    # A print statement that prints the number of the chosen symbol twice plus 1 for every character in the text imputed
    print(deco_type * num_of_deco * 2 + deco_type * len(input_text))


# Calls the decorator function and decorates the text in this case Test_text with 2 & symbols on either side, above and bellow
decorator("Test_text 1", 4, "*")

decorator("Test_text 2", 7, "!")

decorator("Test_text 3", 2, "&")



