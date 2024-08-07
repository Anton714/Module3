calls = 0

def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string_):
    count_calls()
    tuple_ = (len(string_), string_.upper(), string_.lower())
    return tuple_


def is_contains(string_, list_to_search):
    count_calls()
    list_to_search_lower = []

    string_1 = string_.lower()
    for i in range(len(list_to_search)):
        list_to_search_i = list_to_search[i]
        list_to_search_lower.append(list_to_search_i.lower())

    if string_1 in list_to_search_lower:
        return True

    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
