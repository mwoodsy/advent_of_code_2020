import time
start_time = time.time()


def getNSpoken(d, n):
    game = d.split(",")
    seen = {}
    valueAt = []
    
    for i in range(len(game)-1):
        seen[game[i]] = i+1
        game[i] = int(game[i])
    game[-1] = int(game[-1])
    offset = len(game)
    last = game[-1]
    game = game[:-1]
    for i in range(n-offset):
        k = i + offset
        try:
            y = seen[str(last)]
            seen[str(last)] = k
            #print(seen)
            #print(k,y,last)
            game.append(last)
            last = k-y
        except:
            seen[str(last)] = k
            #valueAt.append(k)
            game.append(last)
            last = 0
    #print(game)
    return last


data = '0,13,16,17,1,10,6'


print("Part 1: %s" % getNSpoken(data, 2020))
print("Part 2: %s" % getNSpoken(data, 30000000))

print("--- %s seconds ---" % (time.time() - start_time))