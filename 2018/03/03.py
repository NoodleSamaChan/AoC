class Claim:
    def __init__(self, line):
        id_split = line.split("@")
        self.id = int(id_split[0].strip(' #'))

        left_edge_split = id_split[1].split(",")
        self.left_edge = int(left_edge_split[0].strip(' '))

        top_split = left_edge_split[1].split(":")
        self.top_edge = int(top_split[0])

        width_split = top_split[1].split("x")
        self.width= int(width_split[0].strip(' '))

        self.height = int(width_split[1].strip(' \n'))
    
    def __str__(self):
        return f"ID: {self.id}, Left edge : {self.left_edge}, Top edge : {self.top_edge}, width : {self.width}, height : {self.height}"
    
    def coordinates(self):
        coordinate = []
        for x in range(self.left_edge,self.left_edge+self.width):
            for y in range(self.top_edge, self.top_edge + self.height):
                coordinate.append((x, y))

        return coordinate   

def parse(file_to_open):
    with open(file_to_open, 'r') as file:
        claims_to_check = []
        for line in file:
            line = Claim(line)
            claims_to_check.append(line)
        return claims_to_check
    
list_to_check = parse('/Users/lunaferraraccio/Desktop/lille/advent_of_code/2018/03/input')
grid = {}
for claim in list_to_check:
    for coord in claim.coordinates():
        if grid.get(coord) == None:
            grid[coord] = [claim.id]
        else:
            grid[coord].append(claim.id)

for y in range(9):
    for x in range(11):
        cell = grid.get((x,y))
        if cell == None:
            print('.', end='')
        elif len(cell) == 1:
            print(cell[0], end='')
        else:
            print('X', end='')
    print('')

counter = 0
for i in grid:
    if len(grid[i]) > 1:
        counter += 1
print(counter)