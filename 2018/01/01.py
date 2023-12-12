with open('/Users/lunaferraraccio/Desktop/lille/advent_of_code/2018/01/input', 'r') as file:
    file_to_check = list(file)
    result = 0
    list_of_results = set()
    duplicates = []

    while duplicates == []:
        for i in range(len(file_to_check)):
            result = result + int(file_to_check[i])
            if result in list_of_results:
                duplicates.append(result)
                break
            else:
                list_of_results.add(result)       
    print(duplicates)