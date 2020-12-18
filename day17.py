import time
start_time = time.time()
import numpy as np
import collections
import copy


datafile = 'data/day17.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

width = len(data[0])
hieght = len(data)
n = 30
sky = np.empty((n,n,n), dtype=str)

x = (n//2)-(width//2)
for d in data:
    y = (n//2)-(hieght//2)
    for i in d:
        sky[x][y][n//2] = i
        y+=1
    x+=1

def getValue(a,b,c,s):
    t = n-1
    if a < 0 or b < 0 or c < 0 or a > t or b > t or c > t:
        return 'n'
    return s[a][b][c]

def loopSky(loops,s):
    while 0 < loops:
        loops -= 1
        tempSky = np.empty((n,n,n), dtype=str)
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    temp = ""
    
                    temp += getValue(j-1,k-1,l-1,s)
                    temp += getValue(j-1,k-1,l,s)
                    temp += getValue(j-1,k-1,l+1,s)
                    temp += getValue(j-1,k,l-1,s)
                    temp += getValue(j-1,k,l,s)
                    temp += getValue(j-1,k,l+1,s)
                    temp += getValue(j-1,k+1,l-1,s)
                    temp += getValue(j-1,k+1,l,s)
                    temp += getValue(j-1,k+1,l+1,s)
                    temp += getValue(j,k-1,l-1,s)
                    temp += getValue(j,k-1,l,s)
                    temp += getValue(j,k-1,l+1,s)
                    temp += getValue(j,k,l-1,s)
                    temp += getValue(j,k,l+1,s)
                    temp += getValue(j,k+1,l-1,s)
                    temp += getValue(j,k+1,l,s)
                    temp += getValue(j,k+1,l+1,s)
                    temp += getValue(j+1,k-1,l-1,s)
                    temp += getValue(j+1,k-1,l,s)
                    temp += getValue(j+1,k-1,l+1,s)
                    temp += getValue(j+1,k,l-1,s)
                    temp += getValue(j+1,k,l,s)
                    temp += getValue(j+1,k,l+1,s)
                    temp += getValue(j+1,k+1,l-1,s)
                    temp += getValue(j+1,k+1,l,s)
                    temp += getValue(j+1,k+1,l+1,s)

                    if(s[j][k][l] == '#'):
                        if(temp.count('#')==2 or temp.count('#')==3):
                            tempSky[j][k][l] = '#'
                        else:
                            tempSky[j][k][l] = '.'
                    else:
                        if(temp.count('#')==3):
                            tempSky[j][k][l] = '#'
                        else:
                            tempSky[j][k][l] = '.'
        s = copy.deepcopy(tempSky)
    
    return copy.deepcopy(s)
                

sky2 = loopSky(6,copy.deepcopy(sky))
part1 = 0
for j in range(n):
    for k in range(n):
        for l in range(n):
            if sky2[j][k][l] == '#':
                part1 += 1

print("Part 1: %s" % part1)


n = 20
sky3 = np.empty((n,n,n,n), dtype=str)

x = (n//2)-(width//2)
for d in data:
    y = (n//2)-(hieght//2)
    for i in d:
        sky3[x][y][n//2][n//2] = i
        y+=1
    x+=1


def getValue2(a,b,c,d,s2):
    t = n-1
    if a < 0 or b < 0 or c < 0 or d < 0 or a > t or b > t or c > t or d > t:
        return '.'
    return s2[a][b][c][d]

def loopSky2(loops,s2):
    while 0 < loops:
        loops -= 1
        tempSky2 = np.empty((n,n,n,n), dtype=str)
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for w in range(n):
                        temp = ""
            
                        temp += getValue2(j-1,k-1,l-1,w,s2)
                        temp += getValue2(j-1,k-1,l,w,s2)
                        temp += getValue2(j-1,k-1,l+1,w,s2)
                        temp += getValue2(j-1,k,l-1,w,s2)
                        temp += getValue2(j-1,k,l,w,s2)
                        temp += getValue2(j-1,k,l+1,w,s2)
                        temp += getValue2(j-1,k+1,l-1,w,s2)
                        temp += getValue2(j-1,k+1,l,w,s2)
                        temp += getValue2(j-1,k+1,l+1,w,s2)
                        temp += getValue2(j,k-1,l-1,w,s2)
                        temp += getValue2(j,k-1,l,w,s2)
                        temp += getValue2(j,k-1,l+1,w,s2)
                        temp += getValue2(j,k,l-1,w,s2)
                        temp += getValue2(j,k,l+1,w,s2)
                        temp += getValue2(j,k+1,l-1,w,s2)
                        temp += getValue2(j,k+1,l,w,s2)
                        temp += getValue2(j,k+1,l+1,w,s2)
                        temp += getValue2(j+1,k-1,l-1,w,s2)
                        temp += getValue2(j+1,k-1,l,w,s2)
                        temp += getValue2(j+1,k-1,l+1,w,s2)
                        temp += getValue2(j+1,k,l-1,w,s2)
                        temp += getValue2(j+1,k,l,w,s2)
                        temp += getValue2(j+1,k,l+1,w,s2)
                        temp += getValue2(j+1,k+1,l-1,w,s2)
                        temp += getValue2(j+1,k+1,l,w,s2)
                        temp += getValue2(j+1,k+1,l+1,w,s2)

                        temp += getValue2(j-1,k-1,l-1,w-1,s2)
                        temp += getValue2(j-1,k-1,l,w-1,s2)
                        temp += getValue2(j-1,k-1,l+1,w-1,s2)
                        temp += getValue2(j-1,k,l-1,w-1,s2)
                        temp += getValue2(j-1,k,l,w-1,s2)
                        temp += getValue2(j-1,k,l+1,w-1,s2)
                        temp += getValue2(j-1,k+1,l-1,w-1,s2)
                        temp += getValue2(j-1,k+1,l,w-1,s2)
                        temp += getValue2(j-1,k+1,l+1,w-1,s2)
                        temp += getValue2(j,k-1,l-1,w-1,s2)
                        temp += getValue2(j,k-1,l,w-1,s2)
                        temp += getValue2(j,k-1,l+1,w-1,s2)
                        temp += getValue2(j,k,l-1,w-1,s2)
                        temp += getValue2(j,k,l+1,w-1,s2)
                        temp += getValue2(j,k+1,l-1,w-1,s2)
                        temp += getValue2(j,k+1,l,w-1,s2)
                        temp += getValue2(j,k+1,l+1,w-1,s2)
                        temp += getValue2(j+1,k-1,l-1,w-1,s2)
                        temp += getValue2(j+1,k-1,l,w-1,s2)
                        temp += getValue2(j+1,k-1,l+1,w-1,s2)
                        temp += getValue2(j+1,k,l-1,w-1,s2)
                        temp += getValue2(j+1,k,l,w-1,s2)
                        temp += getValue2(j+1,k,l+1,w-1,s2)
                        temp += getValue2(j+1,k+1,l-1,w-1,s2)
                        temp += getValue2(j+1,k+1,l,w-1,s2)
                        temp += getValue2(j+1,k+1,l+1,w-1,s2)
                        temp += getValue2(j,k,l,w-1,s2)

                        temp += getValue2(j-1,k-1,l-1,w+1,s2)
                        temp += getValue2(j-1,k-1,l,w+1,s2)
                        temp += getValue2(j-1,k-1,l+1,w+1,s2)
                        temp += getValue2(j-1,k,l-1,w+1,s2)
                        temp += getValue2(j-1,k,l,w+1,s2)
                        temp += getValue2(j-1,k,l+1,w+1,s2)
                        temp += getValue2(j-1,k+1,l-1,w+1,s2)
                        temp += getValue2(j-1,k+1,l,w+1,s2)
                        temp += getValue2(j-1,k+1,l+1,w+1,s2)
                        temp += getValue2(j,k-1,l-1,w+1,s2)
                        temp += getValue2(j,k-1,l,w+1,s2)
                        temp += getValue2(j,k-1,l+1,w+1,s2)
                        temp += getValue2(j,k,l-1,w+1,s2)
                        temp += getValue2(j,k,l+1,w+1,s2)
                        temp += getValue2(j,k+1,l-1,w+1,s2)
                        temp += getValue2(j,k+1,l,w+1,s2)
                        temp += getValue2(j,k+1,l+1,w+1,s2)
                        temp += getValue2(j+1,k-1,l-1,w+1,s2)
                        temp += getValue2(j+1,k-1,l,w+1,s2)
                        temp += getValue2(j+1,k-1,l+1,w+1,s2)
                        temp += getValue2(j+1,k,l-1,w+1,s2)
                        temp += getValue2(j+1,k,l,w+1,s2)
                        temp += getValue2(j+1,k,l+1,w+1,s2)
                        temp += getValue2(j+1,k+1,l-1,w+1,s2)
                        temp += getValue2(j+1,k+1,l,w+1,s2)
                        temp += getValue2(j+1,k+1,l+1,w+1,s2)
                        temp += getValue2(j,k,l,w+1,s2)

                        if(s2[j][k][l][w] == '#'):
                            if(temp.count('#')==2 or temp.count('#')==3):
                                tempSky2[j][k][l][w] = '#'
                            else:
                                tempSky2[j][k][l][w] = '.'
                        else:
                            if(temp.count('#')==3):
                                tempSky2[j][k][l][w] = '#'
                            else:
                                tempSky2[j][k][l][w] = '.'
        s2 = copy.deepcopy(tempSky2)
    
    return copy.deepcopy(s2)
                

sky4 = loopSky2(6,copy.deepcopy(sky3))
part2 = 0
for j in range(n):
    for k in range(n):
        for l in range(n):
            for m in range(n):
                if sky4[j][k][l][m] == '#':
                    part2 += 1

print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))