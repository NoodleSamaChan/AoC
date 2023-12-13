def parse(file_to_open):
    with open(file_to_open, 'r') as file:
        string_to_convert = ''
        for i in file:
            string_to_convert = string_to_convert + i
        splitted_list = string_to_convert.split("\n")
        return splitted_list

list_to_check = parse('/Users/lunaferraraccio/Desktop/lille/advent_of_code/2018/02/input')

def duplication_checker(elements_to_check):
    nb_of_doubles = 0
    nb_of_triples = 0
    doubles = 0
    triples = 0
    for i in elements_to_check:
        for j in i:
            if i.count(j) == 2:
                doubles = 1
            elif i.count(j) == 3:
                triples = 1
        if doubles == 1:
            nb_of_doubles += 1
            doubles = 0
        if triples == 1:
            nb_of_triples += 1
            triples = 0
    return nb_of_doubles, nb_of_triples

a, b = duplication_checker(list_to_check)

result = a * b
print(result)

def two_almost_same(new_element_to_check):
    nb_of_differences = 0
    for i in new_element_to_check:
        for j in new_element_to_check:
            for k in range(len(i)):
                if i[k] != j[k]:
                    nb_of_differences += 1    
            if nb_of_differences == 1:
                return (i, j)
            else:
                nb_of_differences = 0

result_p2 = two_almost_same(list_to_check)
print(result_p2)
final_to_check = list(result_p2)

def difference_replacer(elements_to_check):
    final_string = ''
    for i in elements_to_check:
        for j in elements_to_check:
            for k in range(len(i)):
                if i[k] != j[k]:
                    final_string = i.replace(i[k], '')

    return final_string

final_string_result = difference_replacer(final_to_check)
print(final_string_result)
