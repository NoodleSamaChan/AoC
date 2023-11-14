with open('2022/02/input_2', 'r') as file:
    score = 0
    for line in file:
        if line[0] == 'A':
            if line[2] == 'X':
                score = score + 3 + 1
            elif line[2] == 'Y':
                score = score + 6 + 2
            elif line[2] == 'Z':
                score = score + 0 + 3
        elif line [0] == 'B':
            if line[2] == 'X':
                score = score + 0 + 1
            elif line[2] == 'Y':
                score = score + 3 + 2
            elif line[2] == 'Z':
                score = score + 6 + 3
        else:
            if line[2] == 'X':
                score = score + 6 + 1
            elif line[2] == 'Y':
                score = score + 0 + 2
            elif line[2] == 'Z':
                score = score + 3 + 3
    print(score)
    
with open('2022/02/input_2', 'r') as file:
    score_2 = 0
    for line_2 in file:
        if line_2[0] == 'A':
            if line_2[2] == 'X':
                score_2 = score_2 + 0 + 3
            elif line_2[2] == 'Y':
                score_2 = score_2 + 3 + 1
            elif line_2[2] == 'Z':
                score_2 = score_2 + 6 + 2
        elif line_2 [0] == 'B':
            if line_2[2] == 'X':
                score_2 = score_2 + 0 + 1
            elif line_2[2] == 'Y':
                score_2 = score_2 + 3 + 2
            elif line_2[2] == 'Z':
                score_2 = score_2 + 6 + 3
        else:
            if line_2[2] == 'X':
                score_2 = score_2 + 0 + 2
            elif line_2[2] == 'Y':
                score_2 = score_2 + 3 + 3
            elif line_2[2] == 'Z':
                score_2 = score_2 + 6 + 1
    print(score_2)