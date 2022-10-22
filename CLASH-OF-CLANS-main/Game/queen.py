import os
from re import X
import time
from colorama import init, Fore, Back, Style

from object import scenery

from object import scenery
from object import obs
from board import *
from object import disappear
from config import *

class queen: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.health=100
    def king_reset(self):
        self.x=70
        self.y=7
        self.health=100
    def move_up(self,a,x,y,m):
        if y == 1 :
            return y
        y=y-1
        if(a[y][x]==' '):
            a[y][x]='Q'
            a[y+1][x]=' '
            if(m==1):
                self.y = y
                return y
            else:
                y=y-1
                if(y>33):
                   y=33
                if(y<1):
                    y=1
                if(a[y][x]==' '):
                    a[y][x]='Q'
                    a[y+1][x]=' '
                    self.y = y
                    return y
                self.y = y + 1
                return y+1
        self.y = y + 1
        return y+1


    def move_down(self,a,x,y,m):
        
        if(y==32):
            return y
        y=y+1
        if(a[y][x]==' '):
            a[y][x]='Q'
            a[y-1][x]=' '
            if(m==1):
                self.y=y
                return y
            else:
                y=y+1
                if(y>33):
                   y=33
                if(y<1):
                    y=1
                if(a[y][x]==' '):
                    a[y][x]='Q'
                    a[y-1][x]=' '
                    self.y=y
                    return y
                self.y=y-1
                return y-1
        self.y=y-1
        return y-1



    def move_left(self,a,x,y,m):
        
        if(x==1):return 1
        x=x-1
        
        if(a[y][x]==' '):
            a[y][x]='Q'
            a[y][x+1]=' '
            if(m==1):
                self.x=x
                return x
            else:
                x=x-1
                if(x<1):
                    x=1
                if(a[y][x]==' '):
                    a[y][x]='Q'
                    a[y][x+1]=' '
                    self.x=x
                    return x
                self.x=x+1
                return x+1
        self.x=x+1
        return x+1


    def move_right(self,a,x,y,m):
        
        if(x==138):return x
        x=x+1
        if(a[y][x]==' ' or a[y][x]=='x'):
            a[y][x]='Q'
            a[y][x-1]=' '
            if(m==1):
                self.x=x
                return x
            else:
                x=x+1
                if(x>138):
                    x=138
                if(a[y][x]==' ' or a[y][x]=='x'):
                    a[y][x]='Q'
                    a[y][x-1]=' '
                    self.x=x
                    return x
                self.x=x-1
                return x-1
        self.x=x-1
        return x-1

    def damage(c1,c2,c3,h1,h2,h3,h4,h5,th,a,b,kp,x1,y1,count,dx):
        xr=x1
        yr=y1
        if(dx==1):
            if(y1-8<=0):
                yr=1
                xr=x1
            else:
                yr=yr-8
        if(dx==2):
            if(x1+8>=140):
                xr=139
                yr=y1
            else:
                xr=xr+8
        if(dx==3):
            if(y1+8>=34):
                yr=33
                xr=y1
            else:
                yr=yr+8
        if(dx==4):
            if(x1-8<=0):
                xr = 1
                yr=y1
            else:
                xr=xr-8
        point=[]
        print(dx)
        print("x1 and x2 are: " + str(x1) + str(y1))
        print("xr and yr are: " + str(xr) + str(yr))
        for el1 in range(xr-2,xr+3,1):
            for el2 in range(yr-2,yr+3,1):
                if((el1>0 and el1<140)and(el2>0 and el2<34)):
                    point.append([el1,el2])
        # print(point)    

        flag = []
        for i in range(16):
            flag.append(False)
        for elem in point:
            print(elem)
            x=elem[0]
            y=elem[1] 
            if(a[y][x]==' ' or a[y][x]=='x'):
                pass
            if(b[y][x][0]=='c' and b[y][x][6]=='1' and flag[0] == False):
                flag[0] = True
                c1[0]=c1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c1[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='c' and b[y][x][6]=='2' and flag[1] == False):
                flag[1] = True
                c2[0]=c2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c2[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='c' and b[y][x][6]=='3' and flag[2] == False):
                flag[2] = True
                c3[0]=c3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c3[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='H' and b[y][x][4]=='1' and flag[3] == False):
                flag[3] = True
                h1[0]=h1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h1[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='H' and b[y][x][4]=='2' and flag[4] == False):
                flag[4] = True
                h2[0]=h2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h2[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='H' and b[y][x][4]=='3' and flag[5] == False):
                flag[5] = True
                h3[0]=h3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h3[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='H' and b[y][x][4]=='4' and flag[6] == False):
                flag[6] = True
                h4[0]=h4[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h4[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='H' and b[y][x][4]=='5' and flag[7] == False):
                flag[7] = True
                h5[0]=h5[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(h5[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='t' and flag[8] == False):
                flag[8] = True
                th[0]=th[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(th[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(len(b[y][x])>7 and b[y][x][0]=='w' and b[y][x][7]=='1' and flag[9] == False):
                flag[9] = True

                w1[0]=w1[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w1[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(len(b[y][x])>7 and b[y][x][0]=='w' and b[y][x][7]=='2' and flag[10] == False):
                flag[10] = True
                w2[0]=w2[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w2[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(len(b[y][x])>7 and b[y][x][0]=='w' and b[y][x][7]=='3' and flag[11] == False):
                flag[11] = True
                w3[0]=w3[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w3[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(len(b[y][x])>7 and b[y][x][0]=='w' and b[y][x][7]=='4' and flag[12] == False):
                flag[12] = True
                w4[0]=w4[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(w4[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1
            if(b[y][x][0]=='c' and b[y][x][6]=='4' and flag[13] == False):
                flag[13] = True
                c4[0]=c4[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(c4[0]<=0):
                    disappear.delete_ele(a,b,b[y][x])
                    count[0]+=1

        