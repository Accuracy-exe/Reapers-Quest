import keyboard as k
import combat as com
import os
import time as t
import Views as v
from entities import entity,mobsp,itemsp
from mods import update, clear, statBar as bar
import mods as m
from mapGenerator import newMap, showMap, spawn, mapDone
from mapGenerator import moveUp as mu, moveRight as mr, moveDown as md, moveLeft as ml
def start():
    def adventure(map):
        delay = 0.1
        clear()
        plr = entity(map)
        print(plr.n.upper())
        print('Health: ', bar(plr.hp, plr.hpcap, 10), plr.hp, '\tLvl',plr.lvl,'-',str(plr.xp)+'/'+str(plr.xpcap), bar(plr.xp, plr.xpcap, 10))
        showMap(map)
        print("Actions:\nUp [W] / Left [A] / Down [S] / Right [D] / Exit [E] : ")
        res = True
        while res:
            plr = entity(map)
            if k.is_pressed('w'):
                clear()
                k.press_and_release('backspace')
                res = mu(map)
                x = m.levelUp(map)
                plr = entity(map)
                print(plr.n.upper())
                print('Health: ', bar(plr.hp, plr.hpcap, 10), plr.hp,'\tLvl',plr.lvl,'-',str(plr.xp)+'/'+str(plr.xpcap), bar(plr.xp, plr.xpcap, 10))
                showMap(map)
                if x!= None:
                    print(x)
                print("Actions:\nUp [W] / Left [A] / Down [S] / Right [D] / Exit [E] : ")
                t.sleep(delay)
            elif k.is_pressed('a'):
                clear()
                k.press_and_release('backspace')
                res = ml(map)
                x = m.levelUp(map)
                plr = entity(map)
                print(plr.n.upper())
                print('Health: ', bar(plr.hp, plr.hpcap, 10), plr.hp,'\tLvl',plr.lvl,'-',str(plr.xp)+'/'+str(plr.xpcap), bar(plr.xp, plr.xpcap, 10))
                showMap(map)
                if x!= None:
                    print(x)
                print("Actions:\nUp [W] / Left [A] / Down [S] / Right [D] / Exit [E] : ")
                t.sleep(delay)
            elif k.is_pressed('s'):
                clear()
                k.press_and_release('backspace')
                res = md(map)
                x = m.levelUp(map)
                plr = entity(map)
                print(plr.n.upper())
                print('Health: ', bar(plr.hp, plr.hpcap, 10), plr.hp,'\tLvl',plr.lvl,'-',str(plr.xp)+'/'+str(plr.xpcap), bar(plr.xp, plr.xpcap, 10))
                showMap(map)
                if x!= None:
                    print(x)
                print("Actions:\nUp [W] / Left [A] / Down [S] / Right [D] / Exit [E] : ")
                t.sleep(delay)
            elif k.is_pressed('d'):
                clear()
                k.press_and_release('backspace')
                res = mr(map)
                x = m.levelUp(map)
                plr = entity(map)
                print(plr.n.upper())
                print('Health: ', bar(plr.hp, plr.hpcap, 10), plr.hp,'\tLvl',plr.lvl,'-',str(plr.xp)+'/'+str(plr.xpcap), bar(plr.xp, plr.xpcap, 10))
                showMap(map)
                if x!= None:
                    print(x)
                print("Actions:\nUp [W] / Left [A] / Down [S] / Right [D] / Exit [E] : ")

                t.sleep(delay)
            elif k.is_pressed('e'):
                if mapDone(map):
                    newMap(map)
                    spawn(map)
                    mobsp(map)
                    itemsp(map)
                    print('\nFloor cleared! Great! Now let\'s move to the next ')
                    t.sleep(5)
                k.press_and_release('backspace')
                break
        if res == False:
            os.remove(f'./PlayerData/{map}.csv')
            os.remove(f'./Map/{map}.txt')
        return res

    m.setup()
    def mainloop():
        plr = entity(user)
        v.infoscreen(plr)
        showMap(user)
        input('Press ENTER to continue your journey...')
        res = adventure(user)
        return res

    while True:
        clear()
        global user
        user = ''
        option = v.homescreen()
        if option == 1:
            clear()
            user = v.storyline()
            m.new_profile(user)
            clear()
            plr = entity(user)
            newMap(user)
            showMap(user)
            print('The area you will be venturing into ^ Good luck')
            input('Press ENTER to start your journey...')
            spawn(user)
            mobsp(user)
            itemsp(user)
            res = adventure(user)

            while res:
                plr1 = entity(user)
                clear()
                v.infoscreen(plr1)
                i = input('Continue? [y,n]\n')
                if i.lower() == 'y':
                    res = mainloop()
                elif i.lower() == 'n':
                    break
                else:
                    print('Invalid input')
        if option == 2:
            clear()
            l = [i[:-4] for i in os.listdir('./PlayerData')]
            l.remove('Zombie')
            l.remove('Witch')
            l.remove('Berserker')
            print("--Players with Saved Data----")
            for i in range(1,len(l)+1):
                print(f'{i}] {l[i-1]}')
            user = input('Loading Data --> Player name: ')
            if os.path.exists('./PlayerData/'+user+'.csv'):
                res = True
                while res:
                    plr = entity(user)
                    clear()
                    v.infoscreen(plr)
                    i = input('Continue? [y,n]\n')
                    if i.lower() == 'y':
                        res = mainloop()
                    elif i.lower() == 'n':
                        break
                    else:
                        print('Invalid input')
            else:
                clear()
                print("[!] Player Data not found :/")
                t.sleep(3)
        if option == 3:
            v.help()



        if option == 4:
            clear()
            print('Thank you for playing! :)')
            t.sleep(5)
            break

start()