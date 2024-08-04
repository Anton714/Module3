calls = 0


def count_calls():
    global calls
    calls += 1



def string_info(string_):

    count_calls()
    tuple_ = (len(string_), string_.upper(), string_.lower())
    print(tuple_)


def is_contains(string_, list_to_search):

    count_calls()

    string_1 = string_.lower()
    if string_1 in list_to_search:
        print('True')
    else:
        print('False')

list_to_search = ['if', 'else', 'while', 'global', 'true']
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
        string_info(string_)
        is_contains(string_, list_to_search)
        print('Количество вызовов функций: ', calls)
        print('************************************')
        print()
        i += 1

print('THE END!')
print('Try again')
