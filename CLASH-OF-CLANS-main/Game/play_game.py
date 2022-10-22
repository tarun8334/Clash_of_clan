import os
import time
from colorama import init, Fore, Back, Style
from archer import * 

from object import CREATE_TOWNHALL, scenery

from object import scenery
from object import obs
from board import board
from input import *
from king import King
from object import disappear
from spell import spell
from canon import canon
from barberian import barberian
from config import *
from archer import *
from balloon import *
from l1 import *
from queen import queen


# king coordinates
print("Press 1 for King")
print("Press 2 for queen")
# a=Get()
a[0] = input()
if(a[0]=='1'):
    king_movement=King(kxp,kyp)
else:
    king_movement=queen(kxp,kyp)

#================= set-up scenery =====================
level1_create()
l1=1
# print(a[0])
# ================= set-up king moment =====================
file = open(f'replays/replay{int(len(os.listdir("replays"))) + 1}.txt', "w")

while(1):
    # 
    x = Get()
    d=input_to(x)
    # os.system("clear") 
    if d == None:
        file.write("-\n")
    else:
        file.write(d+"\n")
    koo=[king_movement.health]
    king_movement.health=canon.attack(kx,ky,r,koo,cp,obj_obs.get_grid(),obj_board.get_grid(),BarbList)
    king_movement.health=canon.wiz_attack(kx,ky,r,koo,wp,obj_obs.get_grid(),obj_board.get_grid(),BarbList,archlist,balloonlist)
    king_movement.health=koo[0]
    for barb in BarbList:
        if barb.health > 0:
            br = obj_obs.get_grid()
            attacking = False
            neighbbors = [(barb.x + i, barb.y + j) for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            for nx, ny in neighbbors:
                if br[ny][nx][0] in ['c', 'H', 't', 'w']:
                    attacking = True
                    barb.attack(obj_board.get_grid(), obj_obs.get_grid(),c1,c2,c3,h1,h2,h3,h4,h5,th,count)
                    break
            if not attacking:
                barb.move(obj_board.get_grid(), obj_obs.get_grid())
    for arch in archlist:
        if arch.health > 0:
            br = obj_obs.get_grid()
            attacking = False
            neighbbors = [(arch.x + i, arch.y + j) for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            for nx, ny in neighbbors:
                if br[ny][nx][0] in ['c', 'H', 't', 'w']:
                    attacking = True
                    arch.attack(obj_board.get_grid(), obj_obs.get_grid(),c1,c2,c3,h1,h2,h3,h4,h5,th,count)
                    break
            if not attacking:
                arch.move(obj_board.get_grid(), obj_obs.get_grid())
    for loon in balloonlist:
        if loon.health > 0:
            br = obj_obs.get_grid()
            attacking = False
            neighbbors = [(loon.x + i, loon.y + j) for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            for nx, ny in neighbbors:
                if br[ny][nx][0] in ['c', 'H', 't', 'w']:
                    attacking = True
                    loon.attack(obj_board.get_grid(), obj_obs.get_grid(),c1,c2,c3,h1,h2,h3,h4,h5,th,count)
                    break
            if not attacking:
                loon.move(obj_board.get_grid(), obj_obs.get_grid())
    array=obj_board.get_grid()
    print(count[0])
    if(count[0]==building_count[0]):
        if(l2==0):
            l2=1
            l1=1
            array[ky][kx]=' '
            kx=70
            ky=7
            king_movement.health=100
            array[ky][kx]='K'
            print("LEVEL 2")
            level2_create()
            continue
        elif(l3==0):
            l3=1
            l1=1
            array[ky][kx]=' '
            kx=70
            ky=7
            king_movement.health=100
            array[ky][kx]='K'
            print("LEVEL 3")
            level3_create()
            continue
        elif(l1==1 and l2==1 and l3==1):
            print("YOU WON")
            break

    if(king_movement.health==0) and len(BarbList)==0:
        print("YOU LOST")
        os.system('aplay -q ./sounds/lose.wav& 2>/dev/null')
        break
    if d == None:
        pass
    elif(d=='1'):
        BarbList.append(barberian(56,2,'barberian 1',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='2'):
        BarbList.append(barberian(56,3,'barberian 2',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='3'):
        BarbList.append(barberian(29,4,'barberian 3',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='4'):
        archlist.append(archer(2,5,'archer 1',600,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='5'):
        archlist.append(archer(2,6,'archer 2',600,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='6'):
        archlist.append(archer(2,7,'archer 3',600,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='7'):
        balloonlist.append(balloon(2,8,'baloon 1',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='8'):
        balloonlist.append(balloon(2,9,'baloon 2',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='9'):
        balloonlist.append(balloon(2,10,'baloon 3',60,obj_board.get_grid(),obj_obs.get_grid()))
    elif(d=='q'):
        break 
    elif(d=='w'):
        dr=1
        ky=king_movement.move_up(obj_board.get_grid(),kx,ky,mo) 
    elif(d=='s'):
        dr=3
        ky=king_movement.move_down(obj_board.get_grid(),kx,ky,mo)
    elif(d=='a'):
        dr=4
        kx=king_movement.move_left(obj_board.get_grid(),kx,ky,mo)
    elif(d=='d'):
        dr=2
        kx=king_movement.move_right(obj_board.get_grid(),kx,ky,mo)
    elif(d=='e'):
        king_movement.health=king_movement.health*2
        if(king_movement.health>100):
            king_movement.health=100
        print(king_movement.health)
    elif(d=='r'):
        kp=spell.rage(kp)
        mo=2
    elif(d=='x'):
        King.damage(c1,c2,c3,h1,h2,h3,h4,h5,th,obj_board.get_grid(),obj_obs.get_grid(),kp,kx,ky,count) 
    elif( a[0]=="1" and d==' '):
        ch=King.check(king_movement,obj_board.get_grid(),kx,ky,obj_obs.get_grid())
        if ch == None:
            pass
        elif(ch[0]=='c'):
            if(ch[6]=='1'):
                c1[0]=c1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c1[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[6]=='2'):
                c2[0]=c2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c2[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[6]=='3'):
                c3[0]=c3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c3[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
        elif(ch[0]=='H'):
            if(ch[4]=='1'):
                h1[0]=h1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h1[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[4]<='2'):
                h2[0]=h2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h2[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[4]=='3'):
                h3[0]=h3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h3[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[4]=='4'):
                h4[0]=h4[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h4[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[4]=='5'):
                h5[0]=h5[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h5[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
        elif(ch[0]=='t'):
            th[0]=th[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(th[0]<=0):
                disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                count[0]+=1
        elif(ch[0]=='w'):
            if(ch[7]=='1'):
                w1[0]=w1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w1[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[7]=='2'):
                w2[0]=w2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w2[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[7]=='3'):
                w3[0]=w3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w3[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
            if(ch[7]=='4'):
                w4[0]=w4[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w4[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
    elif(d==' '):
            queen.damage(c1,c2,c3,h1,h2,h3,h4,h5,th,obj_board.get_grid(),obj_obs.get_grid(),kp,kx,ky,count,dr)
    obj_board.print_board(king_movement,c1,c2,c3,h1,h2,h3,h4,h5,th,obj_obs.get_grid(),king_movement.health, BarbList,w1,w2,w3,w4)
file.close()
        
            
        

    

    




