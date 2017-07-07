import csv

POS="pos"
NAME="name"
SALARY="salary"
POINTS="points"
EFF="eff"
THREES="threes"
REBOUNDS="rebounds"
ASSISTS="assists"
STEALS="steals"
BLOCKS="blocks"
TURNOVERS="turnovers"
FANTASY_POINTS="fantasy"

teams = ['CLE','GSW','BOS','SAS']
TRIPLE_DOUBLE_STATS = [POINTS,REBOUNDS,ASSISTS,STEALS,BLOCKS]

SALARY_CAP=50000
def fetchDKStats(playerStats):
    POSITION_INDX=0
    NAME_INDX=1
    SALARY_INDX=2
    POINTS_INDX=4
    EFF_INDX=5
    csv_path = "C:\\Users\\Zac\\Documents\\Draftkings\\NBA\\DKSalaries.csv"
    players = list()
    with open(csv_path,'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            player = dict()
            player[NAME] = row[NAME_INDX].lower()
            if not player[NAME] in playerStats:
                continue
            player[POS] = row[POSITION_INDX]
            player[SALARY] = int(row[SALARY_INDX])
            player[POINTS] = playerStats[player[NAME]][FANTASY_POINTS]
            player[EFF] = float(player[SALARY] / player[POINTS])
            players.append(player)


    sortedList = sorted(players,key=lambda x: x[EFF],reverse=False)
    return sortedList

def fetchDKStatsWITHDKPOINTS():
    POSITION_INDX=0
    NAME_INDX=1
    SALARY_INDX=2
    POINTS_INDX=4
    EFF_INDX=5
    csv_path = "C:\\Users\\Zac\\Documents\\Draftkings\\NBA\\DKSalaries.csv"
    players = list()
    with open(csv_path,'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            player = dict()
            player[NAME] = row[NAME_INDX].lower()
            player[POS] = row[POSITION_INDX]
            player[SALARY] = int(row[SALARY_INDX])
            player[POINTS] = float(row[POINTS_INDX])
            player[EFF] = float(player[SALARY] / player[POINTS])
            players.append(player)
    sortedList = sorted(players,key=lambda x: x[EFF],reverse=False)
    sortedList = sorted(sortedList,key=lambda x: x[POINTS_INDX],reverse=False)
    return sortedList

def fantastyScore(player):
    score = 0
    score += player[POINTS]
    score += (player[THREES] * .5)
    score += (player[REBOUNDS] * 1.25)
    score += (player[ASSISTS] * 1.5)
    score += (player[STEALS] * 2)
    score += (player[BLOCKS] * 2)
    score -= (player[TURNOVERS] * .5)
    tdDeciderCount = 0
    for k in TRIPLE_DOUBLE_STATS:
        if player[k] >= 7.5:
            tdDeciderCount+=1
    if tdDeciderCount >= 2:
        score += 1.25
    if tdDeciderCount >= 3:
        score += 1.75
    return score

def fetchStats():
    NAME_INDX=1
    TEAM_INDX=4
    MINUTES_INDX=7
    THREE_INDX=11
    REBOUND_INDX=23
    ASSIST_INDX=24
    STEAL_INDX=25
    BLOCK_INDX=26
    TURNOVER_INDX=27
    POINT_INDX=29
    csv_path = "C:\\Users\\Zac\\Documents\\Draftkings\\NBA\\PlayoffStats.csv"
    players = dict()
    with open(csv_path,'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if not row[TEAM_INDX] in teams:
                continue
            player = dict()
            player[POINTS] = float(row[POINT_INDX])
            player[THREES] = float(row[THREE_INDX])
            player[REBOUNDS] = float(row[REBOUND_INDX])
            player[ASSISTS] = float(row[ASSIST_INDX])
            player[STEALS] = float(row[STEAL_INDX])
            player[BLOCKS] = float(row[BLOCK_INDX])
            player[TURNOVERS] = float(row[TURNOVER_INDX])
            player[FANTASY_POINTS] = fantastyScore(player)
            name = row[NAME_INDX].lower()
            if player[FANTASY_POINTS] >= 5:
                players[name] = player
    return players


requiredPositions = ['PG','SG','SF','PF','C','G','F','UTIL']
def craftRoster(players):
    players = sorted(players,key=lambda x: x[POINTS],reverse=False)


def rosterMaker(players,indx,)


playersDict = fetchStats()
playersList = fetchDKStats(playersDict)
craftRoster(playersList)
