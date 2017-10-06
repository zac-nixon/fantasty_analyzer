import json

l = []
for i in range(10):
    print i
    l.append(i)

cores = 3
prevIndex = 0
indx = len(l) / cores
ls = []
for i in range(cores):
    curIndex = prevIndex + indx
    ls.append(l[prevIndex:curIndex])
    prevIndex = curIndex

if len(l) % cores != 0:
    ls[cores - 1].append(l[(len(l) - 1)])

for a in ls:
    print a
