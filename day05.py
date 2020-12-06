import time
start_time = time.time()

datafile = 'data/day05.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

seatValues =[]
occupiedSeats = [0]*(128*8)

for pos in values:
    pos = pos.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    row = int(pos[:7], 2)
    seat = int(pos[7:],2)
    val = row*8+seat 
    seatValues.append(val)
    occupiedSeats[val] = 1

print("Part 1: %s" % max(seatValues))

openSeats = occupiedSeats.index(1)
mySeat = openSeats + occupiedSeats[openSeats:].index(0)

print("Part 2: %s" % mySeat)

print("--- %s seconds ---" % (time.time() - start_time))