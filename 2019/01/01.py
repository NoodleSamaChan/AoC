import math
with open('/home/noodlesama/AoC/2019/01/input', 'r') as file:
    list_to_check = list(file)
    total = 0
    for i in list_to_check:
        fuel_calculation = (math.floor(int(i)/3)) - 2
        if (fuel_calculation/3 - 2) < 0:
            total += fuel_calculation
        else:
            total += fuel_calculation
            while (math.floor(fuel_calculation)/3 - 2) > 0:
                fuel_calculation = (math.floor(fuel_calculation/3) - 2)  
                total += fuel_calculation    
    print(total)