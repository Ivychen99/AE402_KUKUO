# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:24 2021

@author: konan
"""
import pygame,random

def randColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
    
    
    
    
BLACK       = (0  ,0  ,0  )    
WHITE       = (255  ,255  ,255  ) 
GREEN       = (0  ,255  ,0  )
RED         = (255  ,0  ,0  ) 






pygame.init()

size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("滑鼠")

done = False
click = False
count = 0
limit = 30
clock = pygame.time.Clock()

RED = (255,0,0)
x = 0
y = 0


while done == False:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            done = True
        if envent.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            click = True
            count = 0
            color = randColor()
    screen.fill(BLACK) 


    if click == True and count < limit:
        pygame.draw.circle(screen,color,pos,count)
        count = count + 1
        if count >= limit:
            click = False
   
    #pygame.draw.circle(screen,black,(100,50),1,1) #畫一個點半徑1 線寬1>>可畫出一個點
    
   
       
    pygame.display.flip()
    clock.tick(60)
pygame.quit()





#pygame.draw.circle()









