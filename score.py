from player import *
from reader import *
from roster import *
from adjust import *
import sys
from multiprocessing import Process
import random

#Assigns the defense object to the particular player
def correlate(players,m):
        for p in players:
            opposition = p.opposition.replace('@','')
            p.oppositionObj = m[opposition]

def blackList(teams,l):
    for t in teams:
        l = filter(lambda x: x.opposition.replace('@','') != t,l)
    return l

def hashDST(DSTs):
    m = {}
    for d in DSTs:
        m[d.name] = d
    return m

for v in ['qb.csv','rb.csv','wr.csv','te.csv','dst.csv']:
    normalize(v)

QBs = fetchQBs()
RBs = fetchRBs()
WRs = fetchWRs()
TEs = fetchTEs()
DSTs = fetchDSTs()
dMap = hashDST(DSTs)

def correctPoints():
    return 0

#Black list
fList = ['Chi','GB','Was','KC','Mia','NO','Sea','Ind']
QBs = blackList(fList,QBs)
RBs = blackList(fList,RBs)
WRs = blackList(fList,WRs)
TEs = blackList(fList,TEs)
DSTs = blackList(fList,DSTs)

correlate(QBs,dMap)
correlate(RBs,dMap)
correlate(WRs,dMap)
correlate(TEs,dMap)

QBs = filter(lambda x: x.avgpts > 1,QBs)
RBs = filter(lambda x: x.avgpts > 1,RBs)
WRs = filter(lambda x: x.avgpts > 1,WRs)
TEs = filter(lambda x: x.avgpts > 1,TEs)
DSTs = filter(lambda x: x.salary > 2500,DSTs)
#1 QB
#2 RB
#3 WR
#1 TE
#1 FLEX
#1 DST

adjustPlayers(QBs,RBs,WRs,TEs,DSTs)


QBs = filter(lambda x: x.avgpts > 5 and x.salary > 4200,QBs)
RBs = filter(lambda x: x.avgpts > 5 and x.salary > 4200,RBs)
WRs = filter(lambda x: x.avgpts > 5 and x.salary > 4200,WRs)
TEs = filter(lambda x: x.avgpts > 5 and x.salary > 3000,TEs)
DSTs = filter(lambda x: x.salary > 2500,DSTs)

'''
for p in QBs:
    print p

for p in WRs:
    print p

for p in TEs:
    print p

for p in RBs:
    print p
'''
candidates = set()
iters = 100000
if len(sys.argv) > 0:
    iters = int(sys.argv[1])
print iters
for i in range(iters):
    if i % 100000 == 0:
      print i
    stack = random.randint(0,100) > 30
    r = Roster()
    QBLocal = list(QBs)
    WRLocal = list(WRs)
    RBLocal = list(RBs)
    TELocal = list(TEs)
    DSTLocal = list(DSTs)

    qb = random.choice(QBLocal)
    r.addPlayer(qb,False)

    te = random.choice(TELocal)
    r.addPlayer(te,False)

    RBLocal = filter(lambda x: te.team != x.team,RBLocal)
    WRLocal = filter(lambda x: te.team != x.team,WRLocal)
    TELocal = filter(lambda x: te.team != x.team,TELocal)


    if stack:
        sameTeam = filter(lambda x: qb.team == x.team,WRLocal)
        if len(sameTeam) != 0:
            wr1 = random.choice(sameTeam)
        else:
            stack = False

    if not stack:
        wr1 = random.choice(WRLocal)
    r.addPlayer(wr1,False)

    RBLocal = filter(lambda x: wr1.team != x.team,RBLocal)
    WRLocal = filter(lambda x: wr1.team != x.team,WRLocal)
    TELocal = filter(lambda x: wr1.team != x.team,TELocal)

    wr2 = random.choice(WRLocal)
    r.addPlayer(wr2,False)

    RBLocal = filter(lambda x: wr2.team != x.team,RBLocal)
    WRLocal = filter(lambda x: wr2.team != x.team,WRLocal)
    TELocal = filter(lambda x: wr2.team != x.team,TELocal)

    wr3 = random.choice(WRLocal)
    r.addPlayer(wr3,False)

    RBLocal = filter(lambda x: wr3.team != x.team,RBLocal)
    WRLocal = filter(lambda x: wr3.team != x.team,WRLocal)
    TELocal = filter(lambda x: wr3.team != x.team,TELocal)

    rb1 = random.choice(RBLocal)
    r.addPlayer(rb1,False)

    RBLocal = filter(lambda x: rb1.team != x.team,RBLocal)
    WRLocal = filter(lambda x: rb1.team != x.team,WRLocal)
    TELocal = filter(lambda x: rb1.team != x.team,TELocal)

    rb2 = random.choice(RBLocal)
    r.addPlayer(rb2,False)

    RBLocal = filter(lambda x: rb2.team != x.team,RBLocal)
    WRLocal = filter(lambda x: rb2.team != x.team,WRLocal)
    TELocal = filter(lambda x: rb2.team != x.team,TELocal)

    FLEXLocal = WRLocal + RBLocal
    flex = random.choice(FLEXLocal)
    r.addPlayer(flex,True)

    dst = random.choice(DSTLocal)
    r.addPlayer(dst,False)

    if r.isValid and len(r.DST) == 1 and len(r.FLEX) == 1:
        candidates.add(r)
        l = list(candidates)
        l.sort(key=lambda x: x.projectedPoints, reverse=True)
        candidates = set(l[:40])

l = list(candidates)
l.sort(key=lambda x: x.projectedPoints, reverse=True)
output = ""
for r in l:
    output += r.to_csv() + "\n"
    print str(r)

with open("./roster.csv","w") as f:
    f.write(output)
    f.close()
