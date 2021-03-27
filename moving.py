# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:24 2021

@author: konan
"""
import pygame,random



Black = (0,0,0)
White = (255,255,255)
black = (0,0,0)


pygame.init()

size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("方塊")


    
    
    
    
done = False
clock = pygame.time.Clock()

RED = (255,0,0)
x = 0
y = 0


while done == False:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            done = True
    screen.fill(White) 
    pygame.draw.rect(screen ,RED,[x,y,10,10])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 1
    elif keys[pygame.K_RIGHT]:
        x = x + 1
    elif keys[pygame.K_UP]:
        y = y - 1
    elif keys[pygame.K_DOWN]:   
        y = y + 1
    elif keys[pygame.K_SPACE]:
        x = random.randrange(0,700)
        y = random.randrange(0,500)
    else:
        pass
   
    #pygame.draw.circle(screen,black,(100,50),1,1) #畫一個點半徑1 線寬1>>可畫出一個點
    
   
       
    pygame.display.flip()
    clock.tick(60)
pygame.quit()





#pygame.draw.circle()









