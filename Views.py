import time as t
import os
import mods
import entities as ent
import story as s
def homescreen():

    result = """        ____                            _                                __
       / __ \___  ____ _____  ___  ____( )_____   ____ ___  _____  _____/ /_
      / /_/ / _ \/ __ `/ __ \/ _ \/ ___/// ___/  / __ `/ / / / _ \/ ___/ __/
     / _, _/  __/ /_/ / /_/ /  __/ /    (__  )  / /_/ / /_/ /  __(__  ) /_
    /_/ |_|\___/\__,_/ .___/\___/_/    /____/   \__, /\__,_/\___/____/\__/
                    /_/                           /_/
    """
    for i in result:
        print(i,end='')
        t.sleep(0.0000001)

    print()
    t.sleep(0.8)
    print("\t      -CREATORS-")
    t.sleep(0.8)
    print("\tAnumitha (PES2202200688)")
    t.sleep(0.8)
    print("\tArnab    (PES2202200338)")
    t.sleep(0.8)
    print("\tArun     (PES2202200334)")
    t.sleep(0.8)
    print("\tAnushka  (PES2202200340)")
    t.sleep(1)
    mods.clear()
    print(result)
    print()
    print('[+] New game')
    print('[L] Load game')
    print('[-] How to play')
    print('[X] Quit')
    c = input()
    if c == '+':
        return 1
    if c in ['L','l']:
        return 2
    if c == '-':
        return 3
    if c in ['x','X']:
        return 4


def infoscreen(plr):
    mods.clear()
    print(plr.n.upper())
    print()
    frame1 = '--STATS--'
    statData1 = ' Lvl '+str(plr.lvl)+' '+mods.statBar(plr.xp,plr.xpcap,10)+str(plr.xp)+'/'+str(plr.xpcap)+'\t'+str(plr.hp)+'['+mods.statBar(plr.hp,plr.hpcap,10)[1:-1][::-1]+'] : Health'
    statData2 = ' ATK : ' + str(plr.atk) + '\n' + ' DEF : ' + str(plr.d) + '\n' + ' CRIT RATE : ' +str(plr.crit) + '%'
    while len(statData1) > len(frame1):
        frame1 += '-'
    frame2 = '-' * len(statData1)
    print(frame1)
    print(statData1)
    print(statData2)
    print(frame2)
    print()
    frame1 = '--'
    input('Press ENTER...\n')

def storyline():
    print("Hii....Welcome to our game!")
    print("I see it your first time here....Don't worry, we will make it as amusing as possible for you :)")
    print("What would u be like to be called as? ")
    while True:
        plyname=input()
        if plyname in [i[:-4] for i in os.listdir('./PlayerData')]:
            print("[!] Player with this name already exists :/")
        else:
            break
    print('Welcome',plyname,'!')
    s.prologue()
    t.sleep(3)
    return plyname

def help():
    plyrchoice = input("[R] Read story again\n[H] How to play\n[X] Return to title screen\n")
    if plyrchoice.lower() in ['R','r']:
        s.prologue()
        input("Press ENTER to continue")
    elif plyrchoice.lower() in ['h','H']:
        print("""Every player has certain attributes like 
        -> HP (Hitpoints / Health)
        -> HP cap (maximum HP a player can have in their current level)
        -> XP (Experience Points)
        -> XP cap (XP needed to ascend to next level)
        -> ATK (Total Attack Strength)
        -> DEF (Defence, Amount of damage taken reduced)
        -> CRIT (Critical Hit rate, A chance to double the damage you deal)
        
        === MOVEMENT ===
        Player will spawn in a procedurally generated map and can move around Using W A S D keys.
        Pressing E will let you exit the map, saving your game and then quitting or continuing.
        [!] DO NOT press and hold any action key
        Players will notice 'Z' , 'W' , 'B' and '+' on the map. These are the places you will find souls and healing.
        'Z' being the weakest and 'B' being the strongest. To enter into combat or pick up 'heal', simply move to them.
        
        === COMBAT ===
        Combat logic here is pretty simple, just Rock - Paper - Scissors, but the damage dealt and taken is
        scaled off your attack strength (ATK). DEF or 'defense' reduces the damage you take.
        CRIT rate is the chance for the damage dealt to be doubled""")
        input("Press ENTER to continue...")
    elif plyrchoice.lower() in ['x','X']:
        pass
    else :
        print("Enter a valid choice!")




