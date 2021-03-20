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
    pygame.draw.circle(screen,black,(100,50),1,1)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()





#pygame.draw.circle()









