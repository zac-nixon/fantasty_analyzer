from player import *


def adjustPlayers(QBs, RBs, WRs, TEs, DSTs):
    all = QBs + RBs + WRs + TEs + DSTs
    for p in all:
        p.getContribution()
    medianRush = getMedianRushYd(DSTs)
    medianPass = getMedianPassYd(DSTs)
    medianPoint = getMedianPointsAllowed(DSTs)
    medianPassAttempts = getMedianPassAttempts(QBs)
    medianRushAttempts = getMedianRushAttempts(RBs)
    medianRecv = getMedianReceptions(WRs + TEs)
    adjustQB(QBs, medianPass, medianPoint, medianPassAttempts)
    adjustRB(RBs, medianRush, medianRushAttempts)
    adjustReceiver(WRs + TEs, medianPass, medianRecv)


def getMedianRushYd(DSTs):
    DSTs.sort(key=lambda x: x.rush_yd_allowed, reverse=True)
    return DSTs[len(DSTs) / 2].rush_yd_allowed


def getMedianPassYd(DSTs):
    DSTs.sort(key=lambda x: x.pass_yd_allowed, reverse=True)
    return DSTs[len(DSTs) / 2].pass_yd_allowed


def getMedianPointsAllowed(DSTs):
    DSTs.sort(key=lambda x: x.points_allowed, reverse=True)
    return DSTs[len(DSTs) / 2].points_allowed


def getMedianPassAttempts(QBs):
    QBs.sort(key=lambda x: x.attempts, reverse=True)
    return QBs[len(QBs) / 2].attempts


def getMedianRushAttempts(RBs):
    RBs.sort(key=lambda x: x.rushes, reverse=True)
    return RBs[len(RBs) / 2].rushes


def getMedianReceptions(RECs):
    RECs = filter(lambda x: x.recv > 1, RECs)
    RECs.sort(key=lambda x: x.recv, reverse=True)
    return RECs[len(RECs) / 2].recv


def adjustQB(QBs, medianPass, medianPoint, medianPassAttempts):
    for q in QBs:
        oppPass = q.oppositionObj.pass_yd_allowed
        oppPoints = q.oppositionObj.points_allowed
        pointMultiplerFromDef = (
            float(oppPass) / float(medianPass)) + (float(oppPoints) / float(medianPoint))
        pointMultiplerFromAttempts = (
            float(q.attempts) / float(medianPassAttempts))
        finalMultipler = (pointMultiplerFromAttempts +
                          pointMultiplerFromDef) / 2
        q.fantasy_points = q.fantasy_points * finalMultipler


def adjustRB(RBs, medianRushAllowed, medianRushAttempts):
    for r in RBs:
        oppRush = r.oppositionObj.rush_yd_allowed
        pointMultiplerFromDef = float(oppRush) / float(medianRushAllowed)
        pointMultipleFromRushes = (float(r.rushes) / float(medianRushAttempts))
        finalMultipler = (pointMultiplerFromDef + pointMultipleFromRushes) / 2
        r.fantasy_points = r.fantasy_points * finalMultipler


def adjustReceiver(RECs, medianPassAllowed, medianRecv):
    for r in RECs:
        oppPass = r.oppositionObj.pass_yd_allowed
        pointMultiplerFromDef = float(oppPass) / float(medianPassAllowed)
        pointMultipleFromTargets = (float(r.recv) / float(medianRecv))
        finalMultipler = (pointMultiplerFromDef + pointMultipleFromTargets) / 2
        r.fantasy_points = r.fantasy_points * finalMultipler
