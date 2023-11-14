with open('input', 'r') as file:
    calories = 0
    calories_per_elf = []
    number_of_elves = 1

    for line in file:
        if line != '\n':
            line = int(line)
            calories = calories + line
        elif line == '\n':
            calories_per_elf.append(calories)
            calories = 0
            number_of_elves = number_of_elves + 1
    print(number_of_elves)


    biggest_calories = calories_per_elf[0]
    top_three_elves = []

    for number_cal in calories_per_elf:
        if number_cal > biggest_calories:
            biggest_calories = number_cal
    print(biggest_calories)

    top_three_elves.append(biggest_calories)
    calories_per_elf.pop(calories_per_elf.index(biggest_calories))
    biggest_calories = calories_per_elf[0]

    for number_cal in calories_per_elf:
        if number_cal > biggest_calories:
            biggest_calories = number_cal

    top_three_elves.append(biggest_calories)
    calories_per_elf.pop(calories_per_elf.index(biggest_calories))
    biggest_calories = calories_per_elf[0]

    for number_cal in calories_per_elf:
        if number_cal > biggest_calories:
            biggest_calories = number_cal
    top_three_elves.append(biggest_calories)
    print(top_three_elves)
    total_cals_top_three = 0

    for cals in top_three_elves:
        total_cals_top_three = total_cals_top_three + cals
    print('total calories of top three elves is ', total_cals_top_three)