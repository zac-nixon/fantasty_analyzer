from player import *
from reader import *

QBs = fetchQBs()
RBs = fetchRBs()
WRs = fetchWRs()
TEs = fetchTEs()
DSTs = fetchDSTs()

#Black list

#THU
QBs = filter(lambda x: x.opposition.replace('@','') != 'SF' and x.opposition.replace('@','') != 'LA',QBs)
RBs = filter(lambda x: x.opposition.replace('@','') != 'SF' and x.opposition.replace('@','') != 'LA',RBs)
WRs = filter(lambda x: x.opposition.replace('@','') != 'SF' and x.opposition.replace('@','') != 'LA',WRs)
TEs = filter(lambda x: x.opposition.replace('@','') != 'SF' and x.opposition.replace('@','') != 'LA',TEs)
DSTs = filter(lambda x: x.opposition.replace('@','') != 'SF' and x.opposition.replace('@','') != 'LA',DSTs)

#MON
QBs = filter(lambda x: x.opposition.replace('@','') != 'Ari' and x.opposition.replace('@','') != 'Dal',QBs)
RBs = filter(lambda x: x.opposition.replace('@','') != 'Ari' and x.opposition.replace('@','') != 'Dal',RBs)
WRs = filter(lambda x: x.opposition.replace('@','') != 'Ari' and x.opposition.replace('@','') != 'Dal',WRs)
TEs = filter(lambda x: x.opposition.replace('@','') != 'Ari' and x.opposition.replace('@','') != 'Dal',TEs)
DSTs = filter(lambda x: x.opposition.replace('@','') != 'Ari' and x.opposition.replace('@','') != 'Dal',DSTs)

#MON
QBs = filter(lambda x: x.opposition.replace('@','') != 'Jax' and x.opposition.replace('@','') != 'Bal',QBs)
RBs = filter(lambda x: x.opposition.replace('@','') != 'Jax' and x.opposition.replace('@','') != 'Bal',RBs)
WRs = filter(lambda x: x.opposition.replace('@','') != 'Jax' and x.opposition.replace('@','') != 'Bal',WRs)
TEs = filter(lambda x: x.opposition.replace('@','') != 'Jax' and x.opposition.replace('@','') != 'Bal',TEs)
DSTs = filter(lambda x: x.opposition.replace('@','') != 'Jax' and x.opposition.replace('@','') != 'Bal',DSTs)


QBs = filter(lambda x: x.avgpts > 5,QBs)
RBs = filter(lambda x: x.avgpts > 5,RBs)
WRs = filter(lambda x: x.avgpts > 5,WRs)
TEs = filter(lambda x: x.avgpts > 5,TEs)

RBs = filter(lambda x: x.salary <= 7250,RBs)
WRs = filter(lambda x: x.salary <= 4000,WRs)

for w in RBs:
    print w
