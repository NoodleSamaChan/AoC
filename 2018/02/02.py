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