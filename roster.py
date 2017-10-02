from player import *

class Roster:
    def __init__(self):
        #TODO change this back to 50,000
        self.cap = 50000
        self.expenditure = 0
        self.QBs = []
        self.RBs = []
        self.WRs = []
        self.TEs = []
        self.FLEX = []
        self.DST = []
        self.QBLimit = 1
        self.RBLimit = 2
        self.WRLimit = 3
        self.TELimit = 1
        self.FlexLimit = 1
        self.DSTLimit = 1
        self.projectedPoints = 0

    def canAfford(self,player):
        if self.expenditure + player.salary <= self.cap:
            return True
        return False

    def addPlayer(self,player,flex):

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

    def removePlayer(self,player):
        l = []
        if player.position == QB:
            l = self.QBs
        if player.position == RB:
            l = self.RBs
        if player.position == WR:
            l = self.WRs
        if player.position == TE:
            l = self.TEs
        if player.position == DST:
            l = self.DST

        for i, v in enumerate(l):
            if v.name == player.name:
                del l[i]
                return

        for i, v in enumerate(self.FLEX):
            if v.name == player.name:
                del self.FLEX[i]
                return

    def addQB(self,QB):
        if len(self.QBs) + 1 <= self.QBLimit:
            self.QBs.append(QB)
            return True
        return False

    def addRB(self,RB):
        if len(self.RBs) + 1 <= self.RBLimit:
            self.RBs.append(RB)
            return True
        return False

    def addWR(self,WR):
        if len(self.WRs) + 1 <= self.WRLimit:
            self.WRs.append(WR)
            return True
        return False

    def addTE(self,TE):
        if len(self.TEs) + 1 <= self.TELimit:
            self.TEs.append(TE)
            return True
        return False

    def addFLEX(self,FLEX):
        if len(self.FLEX) + 1 <= self.FlexLimit:
            self.FLEX.append(FLEX)
            return True
        return False

    def addDST(self,D):
        if len(self.DST) + 1 <= self.DSTLimit:
            self.DST.append(D)
            return True
        return False

    def isValid(self):
        return len(self.QBs) == self.QBLimit and len(self.RBs) == self.RBLimit and len(self.WRs) == self.WRLimit and len(self.TEs) == self.TELimit and len(self.FLEX) == self.FlexLimit and len(self.DST) == self.DSTLimit and self.expenditure <= self.cap

    def __str__(self):
        s = ""
        for i,v in enumerate(self.QBs):
            s += "QB " + str(i + 1) + ": " + str(v) + "\n"
        for i,v in enumerate(self.RBs):
            s += "RB " + str(i + 1) + ": " + str(v) + "\n"
        for i,v in enumerate(self.WRs):
            s += "WR " + str(i + 1) + ": " + str(v) + "\n"
        for i,v in enumerate(self.TEs):
            s += "TE " + str(i + 1) + ": " + str(v) + "\n"
        for i,v in enumerate(self.FLEX):
            s += "FLEX " + str(i + 1) + ": " + str(v) + "\n"
        for i,v in enumerate(self.DST):
            s += "DST " + str(i + 1) + ": " + str(v) + "\n"

        s += "Cost = " + str(self.expenditure) + "," + str(self.cap) + " projected = " + str(self.projectedPoints)
        return s

    def to_csv(self):
        s = ""
        for i,v in enumerate(self.QBs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i,v in enumerate(self.RBs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i,v in enumerate(self.WRs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i,v in enumerate(self.TEs):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i,v in enumerate(self.FLEX):
            s += v.name + " " + str(v.fantasy_points) + ","
        for i,v in enumerate(self.DST):
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
