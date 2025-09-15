import time
start_time = time.time()


datafile = 'data/day21.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

allergens = {}
allIngredients = []
for x in data:
    d = x.split(" (contains ")
    d[1]= d[1][:-1]
    al = d[1].split(', ')
    for a in al:
        if( a in allergens.keys() ):
            allergens[a] = set(d[0].split())&allergens[a]
        else:
            allergens[a] = set(d[0].split())
    i = d[0].split()

    for c in i:
        allIngredients.append(c)

while True:
    keepGoing = False
    for f1 in allergens:
        if len(allergens[f1]) == 1:
            for i in allergens:
                word = list(allergens[f1])[0]
                print(word, allergens[i])
                if f1 !=i and word in allergens[i]:
                    allergens[i].remove(word)
    for f in allergens:
        if len(allergens[f])>1:
            keepGoing = True
    if not keepGoing:
        break
for x in allergens:
    r = list(allergens[x])[0]
    allIngredients = list(filter(lambda a: a != r, allIngredients))

print("Part 1:", len(allIngredients))
part2 = ""
for i in sorted (allergens) : 
    part2 += list(allergens[i])[0] +','

part2 = part2[:-1]
print("Part 2:",part2)

print("--- %s seconds ---" % (time.time() - start_time))