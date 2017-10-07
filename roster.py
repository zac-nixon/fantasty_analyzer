from player import *
import copy
import json

QBLimit = 1
RBLimit = 2
WRLimit = 3
TELimit = 1
DSTLimit = 1
cap = 50000


class Roster:

    def __init__(self):
        self.expenditure = 0
        self.projectedPoints = 0
        self.QBs = []
        self.RBs = []
        self.WRs = []
        self.TEs = []
        self.DST = []
        self.recommendedFlex = []

    def canAfford(self, player):
        if self.expenditure + player.salary <= cap:
            return True
        return False

    def addPlayer(self, player, flex):

        if not self.canAfford(player):
            return False

        b = False
        if flex:
            b = self.addFLEX(player)
        elif player.position == QB:
            b = self.addQB(player)
        elif player.position == RB:
            b = self.addRB(player)
        elif player.position == WR:
            b = self.addWR(player)
        elif player.position == TE:
            b = self.addTE(player)
        elif player.position == DST:
            b = self.addDST(player)

        if b:
            self.expenditure += player.salary
            self.projectedPoints += player.fantasy_points
        return b

    def popPlayer(self, position):
        if position == QB:
            l = self.QBs
        if position == RB:
            l = self.RBs
        if position == WR:
            l = self.WRs
        if position == TE:
            l = self.TEs
        if position == DST:
            l = self.DST

        p = l.pop()
        self.expenditure -= p.salary
        self.projectedPoints -= p.fantasy_points

    def addQB(self, QB):
        if len(self.QBs) + 1 <= QBLimit:
            self.QBs.append(QB)
            return True
        return False

    def addRB(self, RB):
        if len(self.RBs) + 1 <= RBLimit:
            self.RBs.append(RB)
            return True
        return False

    def addWR(self, WR):
        if len(self.WRs) + 1 <= WRLimit:
            self.WRs.append(WR)
            return True
        return False

    def addTE(self, TE):
        if len(self.TEs) + 1 <= TELimit:
            self.TEs.append(TE)
            return True
        return False

    def addDST(self, D):
        if len(self.DST) + 1 <= DSTLimit:
            self.DST.append(D)
            return True
        return False

    def isValid(self):
        return len(self.QBs) == QBLimit and len(self.RBs) == RBLimit and len(self.WRs) == WRLimit and len(self.TEs) == TELimit and len(self.DST) == DSTLimit and self.expenditure <= cap

    def __str__(self):
        d = {}
        for i, v in enumerate(self.QBs):
            d['QB' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.RBs):
            d['RB' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.WRs):
            d['WR' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.TEs):
            d['TE' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.DST):
            d['DST' + str(i + 1)] = v.to_dict()

        d['Cost'] = str(self.expenditure)
        d['Projected'] = str(self.projectedPoints)

        for i, v in enumerate(self.recommendedFlex):
            d['FLEX' + str(i + 1)] = v.to_dict()

        return json.dumps(d)

    def to_dict(self):
        d = {}
        for i, v in enumerate(self.QBs):
            d['QB' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.RBs):
            d['RB' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.WRs):
            d['WR' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.TEs):
            d['TE' + str(i + 1)] = v.to_dict()
        for i, v in enumerate(self.DST):
            d['DST' + str(i + 1)] = v.to_dict()

        d['Metadata'] = {}
        d['Metadata']['Cost'] = str(self.expenditure)
        d['Metadata']['Projected'] = str(self.projectedPoints)

        for i, v in enumerate(self.recommendedFlex):
            d['Metadata']['FLEX' + str(i + 1)] = v.to_dict()

        return d

    def __hash__(self):
        s = ""
        for v in self.QBs:
            s += v.name
        for v in self.RBs:
            s += v.name
        for v in self.WRs:
            s += v.name
        for v in self.TEs:
            s += v.name
        for v in self.DST:
            s += v.name

        return hash(s)

    def __eq__(self, other):
        h1 = self.__hash__()
        h2 = other.__hash__()
        return h1 == h2

    def __deepcopy__(self, memo):
        r = Roster()
        r.expenditure = copy.deepcopy(self.expenditure)
        r.projectedPoints = copy.deepcopy(self.projectedPoints)
        r.QBs = copy.deepcopy(self.QBs)
        r.RBs = copy.deepcopy(self.RBs)
        r.WRs = copy.deepcopy(self.WRs)
        r.TEs = copy.deepcopy(self.TEs)
        r.DST = copy.deepcopy(self.DST)
        return r
