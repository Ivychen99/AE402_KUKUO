# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:24 2021

@author: konan
"""
import pygame


Black = (0,0,0)
White = (255,255,255)
black = (0,0,0)


pygame.init()

size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()

while done == False:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            done = True
    screen.fill(White)
    #pygame.draw.circle(screen,black,(100,50),1,1) #畫一個點半徑1 線寬1>>可畫出一個點
    pygame.draw.circle(screen,Black,(150,150),130,4)
    pygame.draw.circle(screen,Black,(100,120),25,0)
    pygame.draw.circle(screen,Black,(200,120),25,0)
    pygame.draw.ellipse(screen,Black,[135,130,30,80],0)
    pygame.draw.arc(screen,Black,[80,130,150,120],3.14,0,9)
       
    pygame.display.flip()
    clock.tick(60)
pygame.quit()





#pygame.draw.circle()









