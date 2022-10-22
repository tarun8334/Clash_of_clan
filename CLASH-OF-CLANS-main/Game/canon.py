from config import * 
import os



class canon:
    def attack(x,y,r,kh,cp,b,board,BarbList):
            for ele in canon_pos:
                xc=ele[0]
                yc=ele[1]
                for i in range(-r,r+1):
                    for j in range(-r,r+1):
                        if yc + i >= 0 and yc + i < len(board) and xc + j >= 0 and xc + j < len(board[0]):
                            if board[yc+i][xc+j]== 'K':
                                kh[0] = kh[0] - cp
                                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                            elif board[yc+i][xc+j]== '@' :
                                for k in range(len(BarbList)):
                                    if xc+j == BarbList[k].x and yc+i == BarbList[k].y:
                                        BarbList[k].health = BarbList[k].health - cp
                                        if BarbList[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            BarbList.remove(BarbList[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                        break
                            elif board[yc+i][xc+j] == '➽':
                                for k in range(len(archlist)):
                                    if xc+j == archlist[k].x and yc+i == archlist[k].y:
                                        archlist[k].health = archlist[k].health - cp
                                        if archlist[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            archlist.remove(archlist[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                        break
                            
                                        
    def wiz_attack(x,y,r,kh,cp,b,board,BarbList,archlist,balloonlist):
            for ele in wiz_pos:
                xc=ele[0]
                yc=ele[1]
                for i in range(-r,r+1):
                    for j in range(-r,r+1):
                        if yc + i >= 0 and yc + i < len(board) and xc + j >= 0 and xc + j < len(board[0]):
                            if board[yc+i][xc+j]== 'K' or board[yc+i][xc+j]== 'Q':
                                kh[0] = kh[0] - cp
                                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                            
                            elif board[yc+i][xc+j]== '@':
                                for k in range(len(BarbList)):
                                    if xc+j == BarbList[k].x and yc+i == BarbList[k].y:
                                        BarbList[k].health = BarbList[k].health - wp
                                        if BarbList[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            BarbList.remove(BarbList[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                        break
                            elif board[yc+i][xc+j] == '➽':
                                for k in range(len(archlist)):
                                    if xc+j == archlist[k].x and yc+i == archlist[k].y:
                                        archlist[k].health = archlist[k].health - wp
                                        if archlist[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            archlist.remove(archlist[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                        break
                                    
                            elif board[yc+i][xc+j] == '☠':
                                for k in range(len(balloonlist)):
                                    if xc+j == archlist[k].x and yc+i == balloonlist[k].y:
                                        balloonlist[k].health = balloonlist[k].health - wp
                                        if balloonlist[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            balloonlist.remove(balloonlist[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                        break
                                            
                                        
                                
            
