from player import *
from roster import *
import sys
import copy

LIMIT = 100000
POINT_THRESHHOLD= 150

def addDST(candidates,roster,DSTs):
    for d in DSTs:
        added = roster.addPlayer(d,False)
        if roster.isValid and roster.projectedPoints > POINT_THRESHHOLD and len(roster.FLEX) == 1 and len(roster.DST) == 1:
            candidates.append(copy.deepcopy(roster))
            candidates.sort(key=lambda x: x.projectedPoints, reverse=True)
            candidates = candidates[:LIMIT]
            if len(candidates) == LIMIT:
                for r in candidates:
                    print r
                sys.exit(1)
        if added:
            roster.popPlayer(DST) #Avoiding popping nothing

#Only ever 1 flex
def addFlex(candidates,roster,FLEXs,DSTs):
    FLEXs.sort(key=lambda x: x.fantasy_points, reverse=True)
    if len(FLEXs) > 0 and roster.projectedPoints + FLEXs[0].fantasy_points < 120: #Bail out if we don't think this is a good line up
        print 'bailing'
        return
    for i, flex in enumerate(FLEXs):
        added = roster.addPlayer(flex,True)
        if added:
            addDST(candidates,roster,DSTs)
            roster.popPlayer(FLEX)

#Only ever 1 TE
def addTE(candidates,roster,RBs,WRs,TEs,DSTs):
    if len(TEs) > 0 and roster.projectedPoints + TEs[0].fantasy_points < 90: #Bail out if we don't think this is a good line up
        print 'bailing'
        return
    for i, te in enumerate(TEs):
        added = roster.addPlayer(te,False)
        if added:
            addFlex(candidates,roster,list(WRs + RBs),DSTs)
            roster.popPlayer(TE)

def addRB(candidates,roster,RBs,WRs,TEs,DSTs):
    for i, rb in enumerate(RBs):
        added = roster.addPlayer(rb,False)
        newWR = filter(lambda x: x.team != rb.team,list(WRs))
        newRB = filter(lambda x: x.team != rb.team,list(RBs[i + 1:]))
        if len(roster.RBs) == RBLimit:
            addTE(candidates,roster,RBs[i + 1:],WRs,TEs,DSTs)
            roster.popPlayer(RB)
        elif added:
            addRB(candidates,roster,RBs[i + 1:],WRs,TEs,DSTs)
            roster.popPlayer(RB)

def addWR(candidates,roster,RBs,WRs,TEs,DSTs):
    for i, wr in enumerate(WRs):
        added = roster.addPlayer(wr,False)
        newWR = filter(lambda x: x.team != wr.team,list(WRs[i + 1:]))
        newRB = filter(lambda x: x.team != wr.team,list(RBs))
        if len(roster.WRs) == WRLimit:
            addRB(candidates,roster,newRB,newWR,TEs,DSTs)
            roster.popPlayer(WR)
        elif added:
            addWR(candidates,roster,newRB,newWR,TEs,DSTs)
            roster.popPlayer(WR)
