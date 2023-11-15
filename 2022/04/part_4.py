with open('2022/04/input_4', 'r') as file:
    first_separation = []
    first_section = []
    second_section = []
    converted_list = []
    counter_same_sections = 0
    any_overlap = 0

    for line in file:
        first_separation = line.split(',')

        for line_2 in first_separation:
            first_section = line_2.rsplit('-')
            second_section.append(first_section[0])
            second_section.append(first_section[1])

            if len(second_section) == 4:

                for element in second_section:
                    converted_list.append(element.strip())
                    
                if (int(converted_list[0]) >= int(converted_list[2])) & (int(converted_list[1]) <= int(converted_list[3])):
                    counter_same_sections += 1
                if (int(converted_list[0]) <= int(converted_list[2])) & (int(converted_list[1]) >= int(converted_list[3])):
                    counter_same_sections += 1
                if (int(converted_list[0]) <= int(converted_list[2]) <= int(converted_list[1])) | (int(converted_list[0]) <= int(converted_list[3]) <= int(converted_list[1])) | (int(converted_list[2]) <= int(converted_list[0]) <= int(converted_list[3])) | (int(converted_list[2]) <= int(converted_list[1]) <= int(converted_list[3])):
                    any_overlap += 1
                    print(converted_list)

                first_separation = []
                first_section = []
                second_section = []
                converted_list = []
    print(any_overlap)

    

