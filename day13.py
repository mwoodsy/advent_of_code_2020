import time
start_time = time.time()

datafile = 'data/day13.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

minute = int(data[0])
buses = data[1].split(",")
stops = []
for b in buses:
    if b == 'x':
        stops.append(minute)
    else:
        b = int(b)
        temp = 0
        while True:
            temp += b
            if(temp > minute):
                stops.append(temp % minute)
                break

part1 = int(buses[stops.index(min(stops))]) * min(stops)
print("Part 1: %s" % part1)

from math import gcd

def lcm(x,y):
    return x*y//gcd(x,y)

last = 0
offset = int(buses[0])
part2 = 0
while True:
    t = last
    t += offset
    last = t
    isGood = False
    for b in buses:
        if b == 'x':
            t += 1
        elif ((t%int(b))==0):
            if b == buses[-1]:
                isGood = True
                break
            else:
                offset = lcm(offset,int(b))
                t += 1
        else:
            isGood = False
            break
    if isGood:
        part2 = last
        break






print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))