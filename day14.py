import time
start_time = time.time()

datafile = 'data/day14.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())


print("Part 1: %s" % 1)
print("Part 2: %s" % 2)

print("--- %s seconds ---" % (time.time() - start_time))