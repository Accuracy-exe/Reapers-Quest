import os
from random import randint as r
import entities as ent


def TileCells():
    with open(f"./Map/tile.txt",'r') as f:
        grid = f.readlines()
        rows = {}
        for i in range(len(grid)):
            rows[i+1] = list(grid[i][:-2])
    return rows

def tunnelAI(rows):
    startPos = [r(1,17),r(1,45)]
    curPos = startPos
    rows[startPos[0]][startPos[1]] = ' '
    for i in range(r(800,2000)):
            l = r(1,8)
            turn = r(1,4)
            tdir = r(1,4)
            if curPos[0] > 1 and curPos[0]-l > 1:
                if turn == 1 and tdir == 1:
                    for j in range(l):
                        rows[curPos[0]-1][curPos[1]] = ' '
                        curPos[0] -= 1
            if curPos[1] < 45 and curPos[1]+l < 45:
                if turn == 1 and tdir == 2:
                    for j in range(l):
                        rows[curPos[0]][curPos[1]+1] = ' '
                        curPos[1] += 1

            if curPos[0] < 18 and curPos[0]+l < 18:
                if turn == 1 and tdir == 3:
                    for j in range(l):
                        rows[curPos[0]+1][curPos[1]] = ' '
                        curPos[0] += 1
            if curPos[1] > 1 and curPos[1]-l > 1:
                if turn == 1 and tdir == 4:
                    for j in range(l):
                        rows[curPos[0]][curPos[1]-1] = ' '
                        curPos[1] -= 1
    return rows

def spawn(map):
    with open(f"./Map/{map}.txt",'r') as f:
        grid = f.readlines()
        rows = {}
        for i in range(len(grid)):
            rows[i+1] = list(grid[i][:-1])
    while True:
        spawnPos = [r(2, 17), r(2, 45)]
        curPos = spawnPos
        if rows[curPos[0]][curPos[1]] != '#':
            rows[curPos[0]][curPos[1]] = '@'
            break
    genMap(rows,map)
    
def moveUp(map):
    combatOutcome = True
    try:
        with open(f"./Map/{map}.txt",'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i+1] = list(grid[i][:-1])
        curPos = []
        for i in rows:
            for j in range(len(rows[i])):
                if rows[i][j] == '@':
                    curPos = [i,j]
        if rows[curPos[0]-1][curPos[1]] == ' ':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] - 1][curPos[1]] = '@'
        if rows[curPos[0]-1][curPos[1]] == 'W':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] - 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'W')
        if rows[curPos[0]-1][curPos[1]] == 'Z':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] - 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'Z')
        if rows[curPos[0]-1][curPos[1]] == 'B':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] - 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'B')
        if rows[curPos[0]-1][curPos[1]] == '+':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] - 1][curPos[1]] = '@'
            ent.interaction(map,2,'+')
    except KeyError:
        pass
    genMap(rows,map)
    return combatOutcome


def moveDown(map):
    combatOutcome = True
    try:
        with open(f"./Map/{map}.txt",'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i+1] = list(grid[i][:-1])
        curPos = []
        for i in rows:
            for j in range(len(rows[i])):
                if rows[i][j] == '@':
                    curPos = [i,j]
        if rows[curPos[0] + 1][curPos[1]] == ' ':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] + 1][curPos[1]] = '@'
        if rows[curPos[0] + 1][curPos[1]] == 'W':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] + 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'W')
        if rows[curPos[0] + 1][curPos[1]] == 'Z':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] + 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'Z')
        if rows[curPos[0] + 1][curPos[1]] == 'B':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] + 1][curPos[1]] = '@'
            combatOutcome = ent.interaction(map,1,'B')
        if rows[curPos[0] + 1][curPos[1]] == '+':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0] + 1][curPos[1]] = '@'
            ent.interaction(map,2,'+')
        genMap(rows,map)
    except KeyError:
        pass
    return combatOutcome

def moveRight(map):
    combatOutcome = True
    try:
        with open(f"./Map/{map}.txt",'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i+1] = list(grid[i][:-1])
        curPos = []
        for i in rows:
            for j in range(len(rows[i])):
                if rows[i][j] == '@':
                    curPos = [i,j]
        if rows[curPos[0]][curPos[1] + 1] == ' ':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] + 1] = '@'
        if rows[curPos[0]][curPos[1] + 1] == 'W':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] + 1] = '@'
            combatOutcome = ent.interaction(map,1,'W')
        if rows[curPos[0]][curPos[1] + 1] == 'Z':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] + 1] = '@'
            combatOutcome = ent.interaction(map,1,'Z')
        if rows[curPos[0]][curPos[1] + 1] == 'B':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] + 1] = '@'
            combatOutcome = ent.interaction(map,1,'B')
        if rows[curPos[0]][curPos[1] + 1] == '+':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] + 1] = '@'
            ent.interaction(map,2,'+')
    except KeyError:
        pass
    genMap(rows,map)
    return combatOutcome

def moveLeft(map):
    combatOutcome = True
    try:
        with open(f"./Map/{map}.txt",'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i+1] = list(grid[i][:-1])
        curPos = []
        for i in rows:
            for j in range(len(rows[i])):
                if rows[i][j] == '@':
                    curPos = [i,j]
        if rows[curPos[0]][curPos[1] - 1] == ' ':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] - 1] = '@'
        if rows[curPos[0]][curPos[1] - 1] == 'W':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] - 1] = '@'
            combatOutcome = ent.interaction(map,1,'W')
        if rows[curPos[0]][curPos[1] - 1] == 'Z':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] - 1] = '@'
            combatOutcome = ent.interaction(map,1,'Z')
        if rows[curPos[0]][curPos[1] - 1] == 'B':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] - 1] = '@'
            combatOutcome = ent.interaction(map,1,'B')
        if rows[curPos[0]][curPos[1] - 1] == '+':
            rows[curPos[0]][curPos[1]] = ' '
            rows[curPos[0]][curPos[1] - 1] = '@'
            ent.interaction(map,2,'+')
    except KeyError:
        pass
    genMap(rows,map)
    return combatOutcome
def mapDone(map):
    with open(f"./Map/{map}.txt",'r') as f:
        grid = f.readlines()
        rows = {}
        for i in range(len(grid)):
            rows[i+1] = list(grid[i][:-1])
        res = False
        for i in rows:
            if 'Z' in rows[i] or 'B' in rows[i] or 'W' in rows[i]:
                res = False
                break
            else:
                res = True
    return res
def genMap(rows,map):
    with open(f"./Map/{map}.txt",'w') as f:
        for i in range(1,len(rows)+1):
            for j in range(len(rows[i])):
                f.write(rows[i][j])
            f.write('\n')
def newMap(map):
    genMap(tunnelAI(TileCells()),map)

def showMap(map):
    with open(f"./Map/{map}.txt",'r') as f:
        print(f.read())
