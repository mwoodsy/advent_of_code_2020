import time
start_time = time.time()

datafile = 'data/day01.txt'
with open(datafile) as f:
    values = list(map(int, f.read().splitlines()))

year = 2020

for x in values:
    diff = year - x
    if(diff in values):
        print("Part 1: "+ str(diff*x))
        break

for x in values:
    found = False
    diff = year - x
    for y in values:
        diff2 = diff - y
        if(diff2 > 0 and diff2 in values):
            print("Part 2: "+ str(diff2*x*y))
            found = True
            break
    if(found):
        break

print("--- %s seconds ---" % (time.time() - start_time))