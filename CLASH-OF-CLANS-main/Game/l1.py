import os
import time
from colorama import init, Fore, Back, Style
from archer import archer

from object import CREATE_TOWNHALL, scenery

from object import scenery
from object import obs
from board import board
from config import *
from king import King

class level1_create:
    def __init__(self):
        obj_scenery.create_townhall(obj_board.get_grid(),'townhall')
        obj_scenery.create_canon(obj_board.get_grid(),'canon 1',5,7)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 2',45,26)
        # obj_scenery.create_canon(obj_board.get_grid(),'canon 3',92,12)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 1',15,10)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 2',101,17)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 3',11,19)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 4',98,24)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 5',117,29)
        obj_scenery.create_king(obj_board.get_grid(),'King',kx,ky)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 1',12,7)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 2',23,26)
        # ================= set-up observer =====================
        obj_observer.create_townhall(obj_obs.get_grid(),'townhall')
        obj_observer.create_canon(obj_obs.get_grid(),'canon 1',5,7)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 2',45,26)
        # obj_observer.create_canon(obj_obs.get_grid(),'canon 3',92,12)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 1',15,10)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 2',101,17)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 3',11,19)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 4',98,24)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 5',117,29)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 1',12,7)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 2',23,26)
        

class level2_create:
    def __init__(self):
        obj_board.initialize_board()
        obj_obs.initialize_board()
        obj_scenery = scenery()
        obj_observer = obs()
        
        obj_scenery.board_empty(obj_board.get_grid())
        obj_scenery.create_townhall(obj_board.get_grid(),'townhall')
        obj_scenery.create_canon(obj_board.get_grid(),'canon 1',5,7)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 2',45,26)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 3',92,12)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 1',15,10)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 2',101,17)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 3',11,19)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 4',98,24)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 5',117,29)
        
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 1',12,7)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 2',23,26)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 3',104,26)
        building_count[0]=building_count[0]+2
        canon_pos.append([93,13])
        wiz_pos.append([105,27])
        count[0]=0
        
        # ================= set-up observer =====================
        obj_observer.create_townhall(obj_obs.get_grid(),'townhall')
        obj_observer.create_canon(obj_obs.get_grid(),'canon 1',5,7)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 2',45,26)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 3',92,12)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 1',15,10)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 2',101,17)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 3',11,19)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 4',98,24)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 5',117,29)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 1',12,7)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 2',23,26)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 3',104,26)
        c1[0]=100
        c2[0]=100
        c3[0]=100
        h1[0]=100
        h2[0]=100
        h3[0]=100
        h4[0]=100
        h5[0]=100
        th[0]=100
        w1[0]=100
        w2[0]=100
        BarbList.clear()
        archlist.clear()
        balloonlist.clear()

class level3_create:
    def __init__(self):
        
        kx=kxp
        ky=kyp
        obj_board.initialize_board()
        obj_obs.initialize_board()
        obj_scenery = scenery()
        obj_observer = obs() 
        
        obj_scenery.board_empty(obj_board.get_grid())  
        obj_scenery.create_townhall(obj_board.get_grid(),'townhall')
        obj_scenery.create_canon(obj_board.get_grid(),'canon 1',5,7)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 2',45,26)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 3',92,12)
        obj_scenery.create_canon(obj_board.get_grid(),'canon 4',87,23)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 1',15,10)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 2',101,17)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 3',11,19)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 4',98,24)
        obj_scenery.create_hut(obj_board.get_grid(),'Hut 5',117,29)
        
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 1',12,7)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 2',23,26)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 3',104,26)
        obj_scenery.create_wizard(obj_board.get_grid(),'wizard 4',45,29)
        building_count[0]=building_count[0]+2
        canon_pos.append([88,24])
        wiz_pos.append([46,30])
        count[0]=0
        
        # ================= set-up observer =====================
        obj_observer.create_townhall(obj_obs.get_grid(),'townhall')
        obj_observer.create_canon(obj_obs.get_grid(),'canon 1',5,7)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 2',45,26)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 3',92,12)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 1',15,10)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 2',101,17)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 3',11,19)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 4',98,24)
        obj_observer.create_hut(obj_obs.get_grid(),'Hut 5',117,29)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 1',12,7)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 2',23,26)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 3',104,26)
        obj_observer.create_canon(obj_obs.get_grid(),'canon 4',87,23)
        obj_observer.create_wizard(obj_obs.get_grid(),'wizard 4',45,29)
        c1[0]=100
        c2[0]=100
        c3[0]=100
        h1[0]=100
        h2[0]=100
        h3[0]=100
        h4[0]=100
        h5[0]=100
        th[0]=100
        w1[0]=100
        w2[0]=100
        w3[0]=100
        BarbList.clear()
        archlist.clear()
        balloonlist.clear()
