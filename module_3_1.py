calls = 0


def count_calls():
    global calls
    calls += 1
    # print(calls)


def string_info():
    global string_
    count_calls()
    tuple_ = (len(string_), string_.upper(), string_.lower())
    print(tuple_)


def is_contains():
    global string_
    count_calls()
    list_to_search = ['if', 'else', 'while', 'global', 'true']
    string_1 = string_.lower()
    if string_1 in list_to_search:
        print('True')
    else:
        print('False')


i = 0
while i < 5:
    print("Введите любой оператор из Python")
    print('или ПРОБЕЛ >> ENTER для завершения программы: ')
    string_ = str(input())

    if string_ == ' ':
        break

    elif string_ == '':
        print('Внимательно следуйте подсказкам!')
        print('************************************')
        print()
        i += 1

    else:
        string_info()
        is_contains()
        print('Количество вызовов функций: ', calls)
        print('************************************')
        print()
        i += 1

print('THE END!')
print('Try again')
