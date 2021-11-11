# A function that decorates text that is imputed when it is called
def decorator(input_text, num_of_deco, deco_type):
    # code that sets a variable in this case line1 as the number of the chosen symbol twice plus 1 for every character in
    # the text imputed
    line1 = (deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # code that sets a variable in this case line2 as the number of the chosen symbols on either side of the input text
    # and the input text
    line2 = (deco_type * num_of_deco + input_text + deco_type * num_of_deco)
    # code that sets a variable in this case line3 as the number of the chosen symbol twice plus 1 for every character
    # in the text imputed
    line3 = (deco_type * num_of_deco * 2 + deco_type * len(input_text))
    # returns the 3 lines in a list with \n to put them on separate lines when printed
    return "{}\n{}\n{}".format(line1,line2,line3)


# Calls the decorator function and decorates the text in this case Test_text with 2 & symbols on either side, above and bellow

print(decorator("Test_text 1", 4, "*"))

print(decorator("Test_text 1", 6, "&"))

print(decorator("Test_text 1", 4, "*"))


