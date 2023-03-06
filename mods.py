import csv
import os
def levelUp(n):
    if os.path.exists("./PlayerData/" + n + ".csv"):
        with open('./PlayerData/' + n + '.csv', 'r') as f:
            r = csv.reader(f)
            l = []
            for i in r:
                l.append(i)
            lvl = int(l[0][0])
            hp = int(l[0][1])
            hpcap = int(l[0][2])
            xp = int(l[0][3])
            xpcap = int(l[0][4])
            atk = int(l[0][5])
            d = int(l[0][6])
            crit = int(l[0][7])
        nlvl = lvl + xp//xpcap
        xp = int(xp % xpcap)
        if nlvl == lvl:
            pass
        elif nlvl > lvl:
            for i in range(nlvl-lvl):
                xpcap += int(round(0.3 * xpcap,0))
                hpcap += int(round(0.2 * hpcap,0))
                atk += int(round(0.18 * atk,0))
                hp = hpcap
            if nlvl % 3 == 0:
                d += 5
            if nlvl % 5 == 0:
                crit += 3
            update(n,nlvl,hp,hpcap,xp,xpcap,atk,d,crit)
            return 'Congratulations! You levelled UP! '+str(lvl)+' --> '+str(nlvl)
        else:
            return None
        
        
        
def clear():
    os.system('cls')


def setup():
    if os.path.exists("./PlayerData"):
        pass
    else:
        os.mkdir("./PlayerData")
        with open("./PlayerData/Zombie.csv", "w") as f:
            pen = csv.writer(f)
            pen.writerow([1, 25, 25, 0, 0, 30, 15, 3])
        with open("./PlayerData/Witch.csv", "w") as f:
            pen = csv.writer(f)
            pen.writerow([1, 30, 30, 0, 0, 50, 0, 11])
        with open("./PlayerData/Berserker.csv", "w") as f:
            pen = csv.writer(f)
            pen.writerow([1, 35, 35, 0, 0, 75, 5, 30])
    if os.path.exists("./Map"):
        pass
    else:
        os.mkdir("./Map")
        with open("./Map/tile.txt", "w") as f:
            f.write("""###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################\n""")
def new_profile(name):
    with open("./PlayerData/" + f"{name}" + ".csv", "w") as f:
        pen = csv.writer(f)
        pen.writerow([1, 75, 75,0,50,100,0,5])


def update(name, lvl, hp, hpcap, xp, xpcap, atk, d, crit):
    with open("./PlayerData/"+name+".csv", "w") as f:
        pen = csv.writer(f)
        pen.writerow([lvl,hp,hpcap,xp,xpcap, atk, d, crit])


def statBar(val,maxval,barSize):
    bar = int(maxval / barSize)
    nb = val//bar
    oStr = "["+("-"*nb)+(" "*(barSize-nb)) + "]"
    return oStr
