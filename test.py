#A = ['A1','A2','A3']
#B = ['B1','B2']
#C = ['C1','C2','C3','C4']


def addC(l, C):
    for c in C:
        l.append(c)
        print l
        l.pop()


def addB(l, B, C):
    for i, b in enumerate(B):
        l.append(b)
        if len(l) == 3:
            addC(list(l), C)
        else:
            addB(list(l), B[i + 1:], C)
        l.pop()

A = ['A1', 'A2']
B = ['B1', 'B2', 'B3']
C = ['C1', 'C2']

for a in A:
    l = [a]
    addB(list(l), B, C)
