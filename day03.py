import time
start_time = time.time()

datafile = 'data/day03.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

width = len(values[0])
length = len(values)


def checkpath(right, down):
    rotate = 0
    trees = 0
    for x in range(length):
        if (x%down == 0):
            temp = values[x][rotate]
            rotate = (rotate+right) % width
            if(temp == '#'):
                trees += 1
    return trees

path1 = checkpath(3,1)
print('Part 1: %s' % path1)

path2 = checkpath(1,1)
path3 = checkpath(5,1)
path4 = checkpath(7,1)
path5 = checkpath(1,2)

pathSum = path1 * path2 * path3 * path4 * path5
print('Part 2: %s' % pathSum)

print("--- %s seconds ---" % (time.time() - start_time))