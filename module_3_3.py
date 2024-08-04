#task 1

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()

print_params(b = 25)

print_params(c = [1,2,3])

#task 2

values_list = ['Error',123,True]

values_dict = {'a':'Empty', 'b':False, 'c':777}

print_params(*values_list)

print_params(**values_dict)

#task3

values_list_2 = ['Search',457543]

print_params(*values_list_2, 87)