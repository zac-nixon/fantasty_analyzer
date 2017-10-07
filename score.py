from player import *
from reader import *
from roster import *
from adjust import *
from create import *
import multiprocessing
from multiprocessing import Process
import sys

# Assigns the defense object to the particular player


def correlate(players, m):
    for p in players:
        opposition = p.opposition.replace('@', '')
        p.oppositionObj = m[opposition]


def blackList(teams, l):
    for t in teams:
        l = filter(lambda x: x.opposition.replace('@', '') != t, l)
    return l


def hashDST(DSTs):
    m = {}
    for d in DSTs:
        m[d.name] = d
    return m

for v in ['qb.csv', 'rb.csv', 'wr.csv', 'te.csv', 'dst.csv']:
    normalize(v)

QBs = fetchQBs()
RBs = fetchRBs()
WRs = fetchWRs()
TEs = fetchTEs()
DSTs = fetchDSTs()
dMap = hashDST(DSTs)

# Black list
fList = ['TB', 'NE', 'KC', 'Hou', 'Min', 'Chi']
QBs = blackList(fList, QBs)
RBs = blackList(fList, RBs)
WRs = blackList(fList, WRs)
TEs = blackList(fList, TEs)
DSTs = blackList(fList, DSTs)

correlate(QBs, dMap)
correlate(RBs, dMap)
correlate(WRs, dMap)
correlate(TEs, dMap)

QBs = filter(lambda x: x.avgpts > 1, QBs)
RBs = filter(lambda x: x.avgpts > 1, RBs)
WRs = filter(lambda x: x.avgpts > 1, WRs)
TEs = filter(lambda x: x.avgpts > 1, TEs)
DSTs = filter(lambda x: x.salary > 2500, DSTs)

adjustPlayers(QBs, RBs, WRs, TEs, DSTs)

QBs = filter(lambda x: x.fantasy_points > 10 and x.salary > 4000, QBs)
RBs = filter(lambda x: x.fantasy_points > 7 and x.salary > 4000, RBs)
WRs = filter(lambda x: x.fantasy_points > 7 and x.salary > 4000, WRs)
TEs = filter(lambda x: x.fantasy_points > 3 and x.salary > 3000, TEs)

QBs.sort(key=lambda x: x.fantasy_points, reverse=True)
RBs.sort(key=lambda x: x.fantasy_points, reverse=True)
WRs.sort(key=lambda x: x.fantasy_points, reverse=True)
TEs.sort(key=lambda x: x.fantasy_points, reverse=True)

# Spawn off processes to calculate rosters
cores = multiprocessing.cpu_count()
pid = sys.argv[1]
qbsBrokenDown = []
for i in range(cores):
    qbsBrokenDown.append([])

i = 0
for q in QBs:
    qbsBrokenDown[i].append(q)
    i = (i + 1) % cores

candidates = list()
length = len(qbsBrokenDown[int(pid)])
for i, q in enumerate(qbsBrokenDown[int(pid)]):
    print 'debug: process ' + pid + ' is on qb ' + q.name + ' done % = ' + str(float(i) / float(length))
    roster = Roster()
    roster.addPlayer(q, False)
    addWR(candidates, roster, RBs, WRs, TEs, DSTs, pid)
    candidates = candidates[:100]
    candidates.sort(key=lambda x: x.projectedPoints, reverse=True)

output = []
for r in candidates:
    output.append(r.to_dict())
s = json.dumps(output)
with open("/tmp/rosters-try" + pid, "w") as f:
    print 'debug: process ' + pid + ' is writing file'
    f.write(s)
    f.close()

sys.exit(0)
# Merge the rosters together
candidates = []
for i in range(cores):
    with open("/tmp/rosters" + str(i), "r") as f:
        data = json.load(f)
    for d in data:
        candidates.append(d)
    candidates.sort(key=lambda x: x['Metadata']['Projected'], reverse=True)
    candidates = candidates[:1]

for c in candidates:
    print json.dumps(c)
