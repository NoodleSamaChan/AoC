with open('2021/01/input_1', 'r') as file:
    counter_increase = 0
    current = 0
    for line in file:
        int(line)
        if current < int(line):
            counter_increase += 1
        current = int(line)
    print(counter_increase - 1)

with open('2021/01/part_1_test', 'r') as file:
    results = []
    a = int(file.__next__())
    b = int(file.__next__())
    c = int(file.__next__())
    results.append(a + b + c)

    for line in file:
        a, b, c = b, c, int(line)
        results.append(a + b + c)

    print(results)

    print(counter_increase - 1)