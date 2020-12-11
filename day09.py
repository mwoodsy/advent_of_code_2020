import time
start_time = time.time()

datafile = 'data/day09.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

for x in range(len(data)):
    data[x] = int(data[x])

i,r,part1 = 25, 25, 0
while True:
    found = False
    s = data[i-r:i]
    t = data[i]
    for x in s:
        u = t-x
        if ((u in s) and (u != x)):
            found = True
            break
    if found:
        i += 1
    else:
        part1 = t
        break

print("Part 1: %s" % part1)

head, tail, part2 = 2,0,0
while True:
    t = data[tail:head]
    s = sum(t)
    if(s==part1):
        part2 = min(t) + max(t)
        break
    elif(s<part1):
        head+=1
    else:
        tail+=1

print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))