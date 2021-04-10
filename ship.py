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
 






pygame.init()



screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Ship")


clock = pygame.time.Clock()
background_pos = [0,0]

background_img = pygame.image.load("Saturn.jpg").convert()

player_img = pygame.image.load("Ship.png").convert() #方法method後面澳括號
player_img.set_colorkey(BLACK)
click_Sound = pygame.mixer.Sound("laser.ogg")
pygame.mixer.music.load("Background.mp3")
pygame.mixer.music.play()




done = False
    
while not done:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            done = True
        elif envent.type == pygame.MOUSEBUTTONDOWN:
            click_Sound.play()
    screen.blit(background_img, background_pos)

    player_pos = pygame.mouse.get_pos()

    x = player_pos[0]
    y = player_pos[1]
    
    screen.blit(player_img,[x-50,y-50])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
     


    
   




#pygame.draw.circle()









