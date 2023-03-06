from random import randint as r
from mapGenerator import genMap
import mods
import combat
import csv
import os
class entity:
    n = ""
    lvl = 0
    hp = 0
    hpcap = 0
    xp =0
    xpcap = 0
    atk = 0
    d = 0
    crit = 0
    def __init__(self,name):
        if os.path.exists("./PlayerData/"+name+".csv"):
            with open('./PlayerData/'+name+'.csv','r') as f:
                r = csv.reader(f)
                l=[]
                for i in r:
                    l.append(i)
                self.n = name
                self.lvl = int(l[0][0])
                self.hp = int(l[0][1])
                self.hpcap = int(l[0][2])
                self.xp = int(l[0][3])
                self.xpcap = int(l[0][4])
                self.atk = int(l[0][5])
                self.d = int(l[0][6])
                self.crit = int(l[0][7])
                
def mobsp(map):
    types = {'Berserker':['B',r(0,2)],'Witch':['W',r(0,4)],'Zombie':['Z',r(0,8)]}
    def sp(a):
        with open(f"./Map/{map}.txt",'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i+1] = list(grid[i][:-1])
        while True:
            spawnPos = [r(2, 17), r(2, 45)]
            curPos = spawnPos
            if rows[curPos[0]][curPos[1]] not in ['#']:
                rows[curPos[0]][curPos[1]] = a
                break
        genMap(rows,map)
    for i in types:
        for j in range(types[i][1]):
            sp(i[0])
def itemsp(map):
    types = {'Heal': ['+', r(0, 8)]}
    def sp(a):
        with open(f"./Map/{map}.txt", 'r') as f:
            grid = f.readlines()
            rows = {}
            for i in range(len(grid)):
                rows[i + 1] = list(grid[i][:-1])
        while True:
            spawnPos = [r(2, 17), r(2, 45)]
            curPos = spawnPos
            if rows[curPos[0]][curPos[1]] not in ['#']:
                rows[curPos[0]][curPos[1]] = a
                break
        genMap(rows, map)

    for i in types:
        for j in range(types[i][1]):
            sp(types[i][0])
def interaction(map,typ,obj):
    if typ == 1:
        if obj == 'W':
            if combat.battle(map,'Witch'):
                return True
            else:
                return False
        if obj == 'Z':
            if combat.battle(map,'Zombie'):
                return True
            else:
                return False
        if obj == 'B':
            if combat.battle(map,'Berserker'):
                return True
            else:
                return False
    if typ == 2:
        if obj == '+':
            with open('./PlayerData/'+map+'.csv','r') as f:
                res = csv.reader(f)
                l=[]
                for i in res:
                    l.append(i)
                if int(l[0][1]) + r(5,20) > int(l[0][2]):
                    l[0][1] = l[0][2]
                else:
                    l[0][1] = int(l[0][1]) + r(5,15)
            mods.update(map,l[0][0],l[0][1],l[0][2],l[0][3],l[0][4],l[0][5],l[0][6],l[0][7])
        

        
