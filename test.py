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
    ls.append([])
i = 0
for s in l:
    ls[i].append(s)
    i = (i + 1) % cores

for a in ls:
    print a
