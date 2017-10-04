from player import *
import copy

QBLimit = 1
RBLimit = 2
WRLimit = 3
TELimit = 1
FlexLimit = 1
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
        self.FLEX = []
        self.DST = []

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
        if position == FLEX:
            l = self.FLEX

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

    def addFLEX(self, FLEX):
        if len(self.FLEX) + 1 <= FlexLimit:
            self.FLEX.append(FLEX)
            return True
        return False

    def addDST(self, D):
        if len(self.DST) + 1 <= DSTLimit:
            self.DST.append(D)
            return True
        return False

    def isValid(self):
        return len(self.QBs) == QBLimit and len(self.RBs) == RBLimit and len(self.WRs) == WRLimit and len(self.TEs) == TELimit and len(self.FLEX) == FlexLimit and len(self.DST) == DSTLimit and self.expenditure <= cap

    def __str__(self):
        s = ""
        for i, v in enumerate(self.QBs):
            s += "QB " + str(i + 1) + ": " + str(v) + "\n"
        for i, v in enumerate(self.RBs):
            s += "RB " + str(i + 1) + ": " + str(v) + "\n"
        for i, v in enumerate(self.WRs):
            s += "WR " + str(i + 1) + ": " + str(v) + "\n"
        for i, v in enumerate(self.TEs):
            s += "TE " + str(i + 1) + ": " + str(v) + "\n"
        for i, v in enumerate(self.FLEX):
            s += "FLEX " + str(i + 1) + ": " + str(v) + "\n"
        for i, v in enumerate(self.DST):
            s += "DST " + str(i + 1) + ": " + str(v) + "\n"

        s += "Cost = " + str(self.expenditure) + "," + str(cap) + \
            " projected = " + str(self.projectedPoints)
        return s

    def to_csv(self):
        s = ""
        for i, v in enumerate(self.QBs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i, v in enumerate(self.RBs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i, v in enumerate(self.WRs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i, v in enumerate(self.TEs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i, v in enumerate(self.FLEX):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i, v in enumerate(self.DST):
            s += v.name + " " + str(v.fantasy_points) + ","
        s += str(self.expenditure)
        return s

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
        for v in self.FLEX:
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
        r.FLEX = copy.deepcopy(self.FLEX)
        r.DST = copy.deepcopy(self.DST)
        return r
