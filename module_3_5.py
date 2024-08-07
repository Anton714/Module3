def get_multiplied_digits (number):
    str_number = str(number)
    first = (int(str_number[0:1]))
    # print(str_number)
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))



print(get_multiplied_digits(40203))

#print(get_multiplied_digits(4345323))

# print(get_multiplied_digits(2222222))   #print(2**7)