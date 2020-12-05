import time
start_time = time.time()

import math
datafile = 'data/day05.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

seatValues =[]
r, c = (128, 8) 
seatChart = [[-1 for i in range(c)] for j in range(r)]  

for seat in values:
    row = [0,127]
    column = [0,7]
    for c in seat:
        if (c == "F"):
            row[1] = math.floor((row[0]+row[1])/2)
        elif (c == "B"):
            row[0] = math.ceil((row[0]+row[1])/2)
        elif (c == "R"):
            column[0] = math.ceil((column[0]+column[1])/2)
        else:
            column[1] = math.floor((column[0]+column[1])/2)
    sV = row[0]*8+column[0]
    seatValues.append(sV)
    seatChart[row[0]][column[0]] = sV

print("Part 1: %s" % max(seatValues))

r1 = 0
for x in seatChart:
    s1 = 0
    for y in x:
        if y == -1:
            sv = (r1 * 8) + s1
            if((sv+1) in seatValues):
                if((sv-1) in seatValues):
                    mySeat = sv
                    break
        s1 += 1
    r1 += 1
    
print("Part 2: %s" % mySeat)
print("--- %s seconds ---" % (time.time() - start_time))