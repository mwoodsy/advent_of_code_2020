import time
start_time = time.time()


#card,door = 5764801,17807724
card,door = 5099500,7648211
subject = 7
div = 20201227

def loopSize(c):
    count = 1
    value = 1
    while True:
        value *= subject
        value %= div
        if(value == c):
            return count
        else:
            count += 1

def transform(subject, loop):
    count = 1
    key = 1
    while count <= loop:
        key *= subject
        key %= div
        count += 1
    return key

doorLoop = loopSize(door)
part1 = transform(card, doorLoop)
print("Part 1:", part1)
print("Part 2: Done!" )
print("--- %s seconds ---" % (time.time() - start_time))