with open('/home/noodlesama/AoC/2020/01/input', 'r') as file:
    list_to_check = list(file)
    for i in list_to_check:
        for j in list_to_check:
            for k in list_to_check:
                if int(i) + int(j) + int(k) == 2020:
                    print (int(i)*int(j)*int(k))
                else:
                    continue

