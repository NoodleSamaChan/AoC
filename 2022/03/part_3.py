with open('2022/03/input_3', 'r') as file:
    calculation_priority = 0
    for line in file:
        common_letter_transition = []
        half_len = int(len(line)/2 )
        full_len = int(len(line))
        for i in range(0,half_len):
            for j in range(half_len, full_len):
                if line[i] == line[j]:
                    common_letter_transition.append(line[j])

        for k in range(len(common_letter_transition)):
            if len(common_letter_transition) > 1:
                common_letter_transition.pop()
        
        for letters in common_letter_transition:
            if 97 <= ord(letters) <= 122:
                calculation_priority = calculation_priority + (ord(letters) - 96)
            elif 65 <= ord(letters) <= 90:
                calculation_priority = calculation_priority + (ord(letters) - 38)

with open('2022/03/input_3', 'r') as file:
    lines_to_check = []
    common_letter_group = []
    result = []
    priority = 0
    for line in file:
        lines_to_check.append(line)
        if len(lines_to_check) == 3:
            for l in lines_to_check[0]:
                for m in lines_to_check[1]:
                    for n in lines_to_check[2]:
                        if m == n == l and n != '\n':
                            common_letter_group.append(n)
                            for o in common_letter_group:
                              if o not in result:
                                result.append(o)

            lines_to_check = []
            for letters in result:
                if 97 <= ord(letters) <= 122:
                    priority = priority + (ord(letters) - 96)
                elif 65 <= ord(letters) <= 90:
                    priority = priority + (ord(letters) - 38)
            common_letter_group = []
            result = []
    print(priority)



