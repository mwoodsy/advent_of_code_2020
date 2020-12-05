import time
start_time = time.time()

datafile = 'data/day05.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

seatValues =[]
r, c = (128, 8) 
seatChart = [[-1 for i in range(c)] for j in range(r)]  

for seat in values:
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")

    row = int(seat[:7], 2)
    col = int(seat[7:],2)
    sV = row*8+col 
    seatValues.append(sV)
    seatChart[row][col] = sV

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