with open('/home/noodlesama/AoC/2018/01/input', 'r') as file:
    file_to_check = list(file)
    result = 0
    list_of_results = []
    new_list = []
    duplicates = []

    while duplicates == []:
        for i in range(len(file_to_check)):
            if file_to_check[i][0] == '+':
                result = result + int(file_to_check[i])
                list_of_results.append(result)
            elif file_to_check[i][0] == '-':
                result = result + int(file_to_check[i])
                list_of_results.append(result)
        for number in list_of_results:
            if number not in new_list:
                new_list.append(number)
            else:
                duplicates.append(number)
                break
    print(duplicates)

