import sys
import json
QB = 'QB'
RB = 'RB'
WR = 'WR'
TE = 'TE'
DST = 'DST'
FLEX = 'FLEX'


class Player:

    def __init__(self, position, name, salary, opposition, avgpts, games):
        # Common
        self.position = position
        self.name = name
        self.opposition = opposition
        self.salary = salary
        self.avgpts = avgpts
        self.oppositionObj = None
        self.games = games

        self.team = ""

        # Offense

        # Passing
        self.passing_td = 0
        self.pass_yd = 0
        self.interception = 0
        self.attempts = 0

        # Rushing
        self.rush_td = 0
        self.rush_yd = 0
        self.rushes = 0

        # Recieving
        self.recv_td = 0
        self.recv_yd = 0
        self.recv = 0
        self.targets = 0

        self.fumbles = 0

        # Defense
        self.sack = 0
        self.def_interception = 0
        self.fumb_recovery = 0
        self.def_touchdowns = 0
        self.points_allowed = 0
        self.safety = 0
        self.pass_yd_allowed = 0
        self.rush_yd_allowed = 0

        # Total pts projected
        self.fantasy_points = 0

    def getContribution(self):
        score = self.fumbles * -1
        if self.position == QB:
            score += self.scoreQB()
        elif self.position == RB:
            score += self.scoreRB()
        elif self.position == WR:
            score += self.scoreWR()
        elif self.position == TE:
            score += self.scoreWR()
        elif self.position == DST:
            score += self.scoreDST()
        else:
            print('you fucked up')
            sys.exit(1)
        if self.games == 0:
            score = 0
        self.fantasy_points = score
        return score

    def scoreQB(self):
        score = self.scorePassing()
        score += self.scoreRushing()
        return score

    def scoreRB(self):
        score = self.scoreReceiving()
        score += self.scoreRushing()
        return score

    def scoreWR(self):
        score = self.scoreReceiving()
        return score

    def scorePassing(self):
        score = self.passing_td * 4
        score += self.pass_yd * .04
        score += self.interception * -1
        if self.pass_yd > 300:
            score += 3
        return score

    def scoreRushing(self):
        score = self.rush_td * 6
        score += self.rush_yd * .1
        if self.rush_yd > 100:
            score += 3
        return score

    def scoreReceiving(self):
        score = self.recv_yd * .1
        score += self.recv_td * 6
        score += self.recv * 1
        if self.recv_yd > 100:
            score += 3
        return score

    def scoreDST(self):
        score = self.sack * 1
        score += self.def_interception * 2
        score += self.fumb_recovery * 2
        score += self.def_touchdowns * 6
        score += self.safety * 2

        if self.points_allowed == 0:
            score += 10
        elif self.points_allowed <= 6:
            score += 7
        elif self.points_allowed <= 13:
            score += 4
        elif self.points_allowed <= 20:
            score += 1
        elif self.points_allowed <= 27:
            score += 0
        elif self.points_allowed <= 34:
            score += -1
        else:
            score += -4
        return score

    def __str__(self):
        return "name = " + self.name + " position = " + self.position + " salary = " + str(self.salary) + " pts = " + str(self.fantasy_points) + " $/pt = " + str(self.salary / self.fantasy_points) + " team = " + self.team

    def to_dict(self):
        d = {}
        d['name'] = self.name
        d['position'] = self.position
        d['salary'] = self.salary
        d['points'] = self.fantasy_points
        d['team'] = self.team
        if self.oppositionObj:
            d['opposition'] = self.oppositionObj.name
        return d
