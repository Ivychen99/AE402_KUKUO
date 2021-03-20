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
pygame.display.set_caption("下雪")

snow_list = []

for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    snow_list.append([x,y])
    
    
    
    
done = False
clock = pygame.time.Clock()

while done == False:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            done = True
    screen.fill(Black)
    for i in range(len(snow_list)):
        pygame.draw.circle(screen,White,snow_list[i],2)
        snow_list[i][1] = snow_list[i][1] +1
        
        if snow_list[i][1] > 400:
            y = 0
            snow_list[i][1] = y
            x = random.randrange(0,400)
            snow_list[i][0] = x
    #pygame.draw.circle(screen,black,(100,50),1,1) #畫一個點半徑1 線寬1>>可畫出一個點
    
   
       
    pygame.display.flip()
    clock.tick(60)
pygame.quit()





#pygame.draw.circle()









