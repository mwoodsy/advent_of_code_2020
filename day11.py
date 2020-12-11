import time
start_time = time.time()

datafile = 'data/day11.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())
import copy
for i in range(len(data)):
    data[i] = list(data[i])

width = len(data) - 1
height = len(data[0]) - 1
data2 = copy.deepcopy(data)
def checkSeats(x,y):
    sit = True
    seats = []
    occupied = 0
    if(x>0):
        seats.append(data[x-1][y])
        if(y>0):
            seats.append(data[x-1][y-1])
        if(y<height):
            seats.append(data[x-1][y+1])
    if(x<width):
        seats.append(data[x+1][y])
        if(y<height):
            seats.append(data[x+1][y+1])
        if(y>0):
            seats.append(data[x+1][y-1])

    if(y>0):
        seats.append(data[x][y-1])
    if(y<height):
        seats.append(data[x][y+1])
            
    occupied = seats.count('#')
    empty = seats.count('L')
    return occupied


def updateSeats():
    grid = copy.deepcopy(data)
    x = 0
    while x < len(data):
        y = 0
        while y < len(data[x]):
            
            seat = data[x][y]
            sit = checkSeats(x,y)
            if seat == "L":
                if(sit == 0):
                    grid[x][y] = "#"
            elif seat == "#":
                if(sit >= 4):
                    grid[x][y] = 'L'
            y += 1
        x += 1
    return grid
i = 0    
while True:
    i += 1
    g = updateSeats()
    if g == data:
        break
    data = copy.deepcopy(g)
    

part1 = 0
for x in data:
    part1 += x.count("#")

print("Part 1: %s" % part1)

def getPos1(x,y):
    x1 = x - 1
    y1 = y - 1
    s = '.'
    while (x1 >= 0) and (y1 >= 0):
        s = data2[x1][y1]
        x1 -= 1
        y1 -= 1
        if (s != '.'):
            break
    return s

def getPos2(x,y):
    x1 = x
    y1 = y - 1
    s = '.'
    while (y1 >= 0):
        s = data2[x1][y1]
        y1 -= 1
        if (s != '.'):
            break
    return s

def getPos3(x,y):
    x1 = x + 1
    y1 = y - 1
    s = '.'
    while (x1 <= width) and (y1 >= 0):
        s = data2[x1][y1]
        x1 += 1
        y1 -= 1
        if (s != '.'):
            break
    return s

def getPos4(x,y):
    x1 = x + 1
    y1 = y
    s = '.'
    while (x1 <= width):
        s = data2[x1][y1]
        x1 += 1
        if (s != '.'):
            break
    return s

def getPos5(x,y):
    x1 = x + 1
    y1 = y + 1
    s = '.'
    while (x1 <= width) and (y1 <= height):
        s = data2[x1][y1]
        x1 += 1
        y1 += 1
        if (s != '.'):
            break
    return s

def getPos6(x,y):
    x1 = x
    y1 = y + 1
    s = '.'
    while (y1 <= height):
        s = data2[x1][y1]
        y1 += 1
        if (s != '.'):
            break
    return s

def getPos7(x,y):
    x1 = x - 1
    y1 = y + 1
    s = '.'
    while (x1 >= 0) and (y1 <= height):
        s = data2[x1][y1]
        x1 -= 1
        y1 += 1
        if (s != '.'):
            break
    return s

def getPos8(x,y):
    x1 = x - 1
    y1 = y
    s = '.'
    while (x1 >= 0):
        s = data2[x1][y1]
        x1 -= 1
        if (s != '.'):
            break
    return s

def checkSeats2(x,y):
    
    seats = []
    occupied = 0
    seats.append(getPos1(x,y))
    seats.append(getPos2(x,y))
    seats.append(getPos3(x,y))
    seats.append(getPos4(x,y))
    seats.append(getPos5(x,y))
    seats.append(getPos6(x,y))
    seats.append(getPos7(x,y))
    seats.append(getPos8(x,y))
    occupied = seats.count('#')
    return occupied




def updateSeats():
    grid2 = copy.deepcopy(data2)
    x = 0
    while x < len(data2):
        y = 0
        while y < len(data2[x]):
            seat = data2[x][y]
            sit = checkSeats2(x,y)
            if seat == "L":
                if(sit == 0):
                    grid2[x][y] = "#"
            elif seat == "#":
                if(sit >= 5):
                    grid2[x][y] = 'L'
            y += 1
        x += 1
    return grid2
i = 0    
while True:
    i += 1
    g2 = updateSeats()
    if g2 == data2:
        break
    data2 = copy.deepcopy(g2)
    

part2 = 0
for x in data2:
    part2 += x.count("#")
print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))