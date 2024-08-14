data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def translator(data):
    l = []

    n = 1
    while n > 0:
        for i in range(len(data)):

            data_ = data[i]
            if isinstance(data_, list):
                n += 1
                loc_list = data_
                for j in range(len(loc_list)):
                    l.append(loc_list[j])




            elif isinstance(data_, dict):
                n += 1
                loc_dict = data_
                list__ = list(loc_dict)
                l.extend(list__)

                list__ = list(loc_dict.values())

                l.extend(list__)


            elif isinstance(data_, tuple):

                loc_tuple = data_
                # n += 1
                for j in range(len(loc_tuple)):
                    l.append(loc_tuple[j])

            elif isinstance(data_, set):
                # n += 1

                for j in range(len(data_)):
                    set_n = data_.pop()
                    l.append(set_n)



            else:

                l.append(data_)

        n = n - 1
        # print(l)
        data = l
        l = []
    return data


def calculator(data):
    sum_ = 0
    new_list = translator(data)
    for i in range(len(new_list)):
        if isinstance(new_list[i], int):
            sum_ += new_list[i]
        else:
            sum_ += len(new_list[i])

    return sum_


print(calculator(data_structure))
