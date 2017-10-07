from player import *
from roster import *
import sys
import copy

LIMIT = 100
POINT_THRESHHOLD = 150

def addDST(candidates, roster, FLEXs, DSTs):
    DSTs = filter(lambda x: roster.canAfford(x), DSTs)
    for d in DSTs:
        added = roster.addPlayer(d, False)
        if added and roster.projectedPoints > POINT_THRESHHOLD:
            FLEXs = filter(lambda x: roster.canAfford(x), FLEXs)
            FLEXs.sort(key=lambda x: x.fantasy_points, reverse=True)
            FLEXs = FLEXs[:5]
            if len(FLEXs) > 0:
                copyRoster = copy.deepcopy(roster)
                copyRoster.recommendedFlex = FLEXs
                candidates.append(copyRoster)
                candidates.sort(key=lambda x: x.projectedPoints, reverse=True)
                candidates = candidates[:LIMIT]
        if added:
            roster.popPlayer(DST)  # Avoiding popping nothing




def addTE(candidates, roster, RBs, WRs, TEs, DSTs):
    TEs = filter(lambda x: roster.canAfford(x), TEs)
    # Bail out if we don't think this is a good line up
    if len(TEs) > 0 and roster.projectedPoints + TEs[0].fantasy_points < 130:
        return
    for i, te in enumerate(TEs):
        added = roster.addPlayer(te, False)
        if added:
            addDST(candidates, roster, list(WRs + RBs), DSTs)
            roster.popPlayer(TE)


def addRB(candidates, roster, RBs, WRs, TEs, DSTs):
    for i, rb in enumerate(RBs):
        added = roster.addPlayer(rb, False)
        newWR = filter(lambda x: x.team !=
                       rb.team and roster.canAfford(x), list(WRs))
        newRB = filter(lambda x: x.team !=
                       rb.team and roster.canAfford(x), list(RBs[i + 1:]))
        if len(roster.RBs) == RBLimit:
            addTE(candidates, roster, RBs[i + 1:], WRs, TEs, DSTs)
            roster.popPlayer(RB)
        elif added:
            addRB(candidates, roster, RBs[i + 1:], WRs, TEs, DSTs)
            roster.popPlayer(RB)


def addWR(candidates, roster, RBs, WRs, TEs, DSTs, pid):
    length = len(WRs)
    for i, wr in enumerate(WRs):
        print 'debug: process ' + pid + ' is on wr ' + wr.name + ' done % = ' + str(float(i) / float(length))
        added = roster.addPlayer(wr, False)
        newWR = filter(lambda x: x.team !=
                       wr.team and roster.canAfford(x), list(WRs[i + 1:]))
        newRB = filter(lambda x: x.team !=
                       wr.team and roster.canAfford(x), list(RBs))
        if len(roster.WRs) == WRLimit:
            addRB(candidates, roster, newRB, newWR, TEs, DSTs)
            roster.popPlayer(WR)
        elif added:
            addWR(candidates, roster, newRB, newWR, TEs, DSTs, pid)
            roster.popPlayer(WR)
