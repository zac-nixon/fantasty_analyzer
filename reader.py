import csv
from player import *

def normalize(name):
    return
    content = []
    with open("./csv/"+name,"r") as f:
        content = f.readlines()
        f.close()

    output = ""
    prevLine = ""
    for i, line in enumerate(content):
        if i % 2 == 0:
            prevLine = line.strip()
        else:
            prevLine += line
            output += prevLine

    with open("./csv/"+name,"w") as f:
        f.write(output)
        f.close()

def fetchQBs():
    players = []
    with open("./csv/qb.csv",'r') as f:
        reader = csv.reader(f,delimiter=",",quotechar='"')
        for row in reader:
            player = parseBasics(row,QB,13,14)
            if row[4] != '--':
                #Passing
                player.attempts = int(str(row[4]).replace(',','')) / player.games
                player.pass_yd = int(str(row[6]).replace(',','')) / player.games
                player.interception = int(str(row[7]).replace(',','')) / player.games
                player.passing_td = int(str(row[8]).replace(',','')) / player.games
                #Rushing
                player.rush_yd = int(str(row[9]).replace(',','')) / player.games
                player.rush_td = int(str(row[10]).replace(',','')) / player.games
                player.fumbles = int(str(row[11]).replace(',','')) / player.games
            players.append(player)
    return players

def fetchRBs():
    players = []
    with open("./csv/rb.csv",'r') as f:
        reader = csv.reader(f,delimiter=",",quotechar='"')
        for row in reader:
            player = parseBasics(row,RB,12,13)
            if row[4] != '--':
                #Rushing
                player.rushes = int(str(row[4]).replace(',','')) / player.games
                player.rush_yd = int(str(row[5]).replace(',','')) / player.games
                player.rush_td = int(str(row[6]).replace(',','')) / player.games

                #Recieving
                player.recv = int(str(row[7]).replace(',','')) / player.games
                player.recv_yd = int(str(row[8]).replace(',','')) / player.games
                player.recv_td = int(str(row[9]).replace(',','')) / player.games
                player.fumbles = int(str(row[10]).replace(',','')) / player.games
            players.append(player)
    return players


def fetchWRs():
    players = []
    with open("./csv/wr.csv",'r') as f:
        reader = csv.reader(f,delimiter=",",quotechar='"')
        for row in reader:
            player = parseBasics(row,WR,12,13)
            if row[4] != '--':
                #Recieving
                player.recv = int(str(row[4]).replace(',','')) / player.games
                player.recv_yd = int(str(row[5]).replace(',','')) / player.games
                player.targets = int(str(row[6]).replace(',','')) / player.games
                player.recv_td = int(str(row[7]).replace(',','')) / player.games

                #Rushing
                player.rush_yd = int(str(row[8]).replace(',','')) / player.games
                player.rush_td = int(str(row[9]).replace(',','')) / player.games
                player.fumbles = int(str(row[10]).replace(',','')) / player.games
            players.append(player)
    return players

def fetchTEs():
    players = []
    with open("./csv/te.csv",'r') as f:
        reader = csv.reader(f,delimiter=",",quotechar='"')
        for row in reader:
            player = parseBasics(row,TE,12,13)
            if row[4] != '--':
                #Recieving
                player.recv = int(str(row[4]).replace(',','')) / player.games
                player.recv_yd = int(str(row[5]).replace(',','')) / player.games
                player.targets = int(str(row[6]).replace(',','')) / player.games
                player.recv_td = int(str(row[7]).replace(',','')) / player.games

                #Rushing
                player.rush_yd = int(str(row[8]).replace(',','')) / player.games
                player.rush_td = int(str(row[9]).replace(',','')) / player.games
                player.fumbles = int(str(row[10]).replace(',','')) / player.games
            players.append(player)
    return players

def fetchDSTs():
    players = []
    with open("./csv/dst.csv",'r') as f:
        reader = csv.reader(f,delimiter=",",quotechar='"')
        for row in reader:
            player = parseBasics(row,DST,14,15)
            player.sack = int(row[4]) / player.games
            player.def_interception = int(row[5]) / player.games
            player.fumb_recovery = int(row[6]) / player.games
            player.safety = int(row[7]) / player.games
            player.def_touchdowns = int(row[9]) / player.games
            player.points_allowed = int(str(row[10]).replace(',','')) / player.games
            player.pass_yd_allowed = int(str(row[11]).replace(',','')) / player.games
            player.rush_yd_allowed = int(str(row[12]).replace(',','')) / player.games
            players.append(player)
    return players

def parseBasics(row,pos,ptsPos,salaryPos):
    name = row[0].strip()
    team = ""
    if "," in name:
        chunks = name.split(',')
        name = chunks[0].strip()
        team = chunks[1].strip()
    opposition = row[1].strip()
    if row[3].strip() == '--':
        games = 0
    else:
        games = int(row[3])
    avgpts = float(row[ptsPos].strip())
    salary = int(row[salaryPos].strip())
    p = Player(pos,name,salary,opposition,avgpts,games)
    p.team = team
    return p
