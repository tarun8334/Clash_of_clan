import os
import sys
import termios, tty, time


from colorama import init, Fore, Back, Style
from object import *
from board import *
from king import King

#set up scerery
kxp=70
kyp=7
kx=70
ky=7
obj_board = board(34, 140)
obj_obs =board(34, 140)
obj_board.initialize_board()
obj_obs.initialize_board()
obj_scenery = scenery()
obj_observer = obs()
king_movement=None
kp=20
cp=10
wp=20
dr=0
a=[None]
c1=[100]
c2=[100]
c3=[100]
c4=[100]
h1=[100]
h2=[100]
h3=[100]
h4=[100]
h5=[100]
th=[100]
w1=[100]
w2=[100]
w3=[100]
w4=[100]
l1=0
l2=0
l3=0
mo=1
BarbList = []
archlist = []
balloonlist = []
r=4
count=[0]
building_count=[10]

canon_pos = [
    (6,8),(46,27)
]
wiz_pos = [
    (13,8),(24,27)
]

building_pos = [
    (5,7),(45,26),(92,12),(15,10),(101,17),(11,19),(98,24),(117,29),(68,18)
]

C1DEAD = False