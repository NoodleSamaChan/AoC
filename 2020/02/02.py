with open('/home/noodlesama/AoC/2020/02/input', 'r') as file:
    list_to_check = list(file)
    separated_values = []
    min_max = []
    min = 0
    max = 0
    letter = ''
    correct_passwords = 0
    correct_passwords_part_2 = 0
    for i in list_to_check:
        separated_values = i.split(' ')
        for j in separated_values:
            min_max = j.split('-')
            if min_max[0].isdigit():
                min = min_max[0]
                max = min_max[1]
                min_max.remove(min)
                min_max.remove(max)
            for k in min_max:
                key_letter = k.split(':')
                if key_letter[-1] == '':
                    letter = key_letter[0]
                for l in key_letter:
                    if len(l) > 1:
                        count = l.count(letter)
                        if int(min) <= count <= int(max):
                            correct_passwords += 1
                        if ((l[int(min)-1] == letter) & (l[int(max)-1] != letter)) | ((l[int(min)-1] != letter) & (l[int(max)-1] == letter)):
                            correct_passwords_part_2 += 1
        separated_values = []
        min_max = []
        min = 0
        max = 0
    print('Part 1 is ', correct_passwords, 'part 2 is ', correct_passwords_part_2)