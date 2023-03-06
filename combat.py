import keyboard as k
import mods
from random import choice as ch, randint as r
from mods import update, clear, statBar as bar
from entities import entity
import time as t
def battle(name,mob):
    k.press_and_release('backspace')
    if mob == 'Zombie':
        xpset = r(5,12)
    if mob == 'Witch':
        xpset = r(10,16)
    if mob == 'Berserker':
        xpset = r(14,18)
    plr = entity(name)
    mob = entity(mob)
    mobMaxHp = mob.hpcap
    maxPlrHp = plr.hpcap
    xp = plr.xp
    res = True
    import random
    lm = ''
    while True:
        clear()
        if plr.hp < 0:
            plr.hp = 0
        if mob.hp < 0:
            mob.hp = 0
        print(f"{plr.n} > ",bar(plr.hp,plr.hpcap,10),plr.hp,"|",mob.hp,'['+bar(mob.hp,mob.hpcap,10)[1:-1][::-1]+']',f" < {mob.n}")
        print()

        pcrit = False
        mcrit = False
        cr = list(range(1,101))
        cRez = []
        for i in range(plr.crit):
            x = ch(cr)
            cRez.append(x)
            cr.remove(x)
        for i in cRez:
            if i in range(1,plr.crit + 1):
                pcrit = True
        for i in range(mob.crit):
            x = ch(cr)
            cRez.append(x)
            cr.remove(x)
        for i in cRez:
            if i in range(1,mob.crit + 1):
                mcrit = True
        if pcrit == False:
            pcrit = 1
        elif pcrit == True:
            pcrit = 2
        if mcrit == False:
            mcrit = 1
        elif mcrit == True:
            mcrit = 2
        m = r(1, 3)
        dmg = r(5,20) / 100
        temp = r(1,5) / 100
        d = {1:'Hammer Strike',2:'Precision Thrust',3:'Barrier'}
        print(lm)
        print()
        if plr.hp <= 0:
            print("You died :/ Bot")
            t.sleep(2)
            clear()
            print('[!] GAME OVER T_T')
            t.sleep(5)
            res = False
            break

            
        elif mob.hp <= 0:
            print("Victory! :)")
            xp += xpset
            t.sleep(2)
            res = True
            break

        try:
            i = eval(input(f"1) {d[1]}\n2) {d[2]}\n3) {d[3]}\nAction [1/2/3]: "))
            if str(type(i)) == "<class 'int'>":
                i = int(i)
                if i == 1 and m == 3:
                    lm = f"{mob.n} casted a Barrier and reflected the damage to you...You took {int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit} DMG!"
                    plr.hp -= int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit
                elif i == 1 and m == 2:
                    lm = f"Your strike smashed through {mob.n}'s attack...You dealt {int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * pcrit} DMG!"
                    mob.hp -= int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * pcrit
                elif i == 2 and m == 1:

                    lm = f"{mob.n} sent you flying...You took {int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit} DMG!"
                    plr.hp -= int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit
                elif i == 2 and m == 3:

                    lm = f"You shattered {mob.n}'s Barrier... dealing {int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * mcrit} DMG!"
                    mob.hp -= int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * mcrit
                elif i == 3 and m == 1:

                    lm = f"You casted a powerful Barrier and reflected {mob.n}'s attack... returned {int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * mcrit} DMG!"
                    mob.hp -= int(round((dmg * plr.atk)-(dmg * plr.atk)*(mob.d/100),0)) * mcrit
                elif i == 3 and m == 2:

                    lm = f"{mob.n} shattered your Barrier... You took {int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit} DMG!"
                    plr.hp -= int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit
                elif i == m == 1:
                    lm = f"You and {mob.n} sent each other flying... you took {int(round((temp * mob.atk)-(temp * mob.atk)*(plr.d/100),0)) * mcrit} DMG while {mob.n} took {int(round((temp * plr.atk)-(temp * plr.atk)*(mob.d/100),0)) * mcrit}"
                    mob.hp -= int(round((temp * plr.atk)-(temp * plr.atk)*(mob.d/100),0)) * mcrit
                    plr.hp -= int(round((temp * mob.atk)-(temp * mob.atk)*(plr.d/100),0)) * mcrit
                elif i == m == 2:
                    lm = f"You and {mob.n} stabbed each other... taking {int(round((temp * mob.atk)-(temp * mob.atk)*(plr.d/100),0)) * mcrit} DMG and dealing {int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit} DMG!"
                    mob.hp -= int(round((dmg * mob.atk)-(dmg * mob.atk)*(plr.d/100),0)) * mcrit
                    plr.hp -= int(round((temp * mob.atk)-(temp * mob.atk)*(plr.d/100),0)) * mcrit
                elif i == m == 3:
                    h = random.randint(1,5)
                    lm = f"You and {mob.n} created Barriers and just stood there... healing {h} HP!"
                    plr.hp += h
                    if plr.hp > maxPlrHp:
                        plr.hp = maxPlrHp

                else:
                    lm = "[!] Choose an option from the move list!"
                print()
            else:

                lm = "[!] Enter a valid input!"
                print()
        except (NameError,SyntaxError):
            lm = '[!] Enter a valid input!'
    update(plr.n, plr.lvl,plr.hp,plr.hpcap,xp,plr.xpcap,plr.atk,plr.d,plr.crit)
    mods.levelUp(name)
    clear()
    return res
