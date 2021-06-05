# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:25:53 2021

@author: konan
"""
import pygame, random, math

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    
    def __init__(self,speed,srx,sry,R, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([R*2,R*2])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,color,(R,R),R,0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx,sry)
        direct = random.randint(20,70)
        radian = math.radians(direct)
        self.dx = speed*math.cos(radian)
        self.dy = -speed*math.sin(radian)
        
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <=0 or self.rect.right >=screen.get_width()):
            self.dx = self.dx * (-1)
        elif(self.rect.top <= 0 or self.rect.bottom >= screen.get_height()):
            self.dy = self.dy *(-1)
    def collide(self):
        self.dx = self.dx*(-1)
        self.dy = self.dy*(-1)
            
pygame.init()

screen = pygame.display.set_mode((400,300))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

alllist = pygame.sprite.Group()
ball1  = Ball(8,100,100,15,BLUE)
alllist.add(ball1)
ball2 = Ball(6,200,250,15,RED)
alllist.add(ball2)

clock = pygame.time.Clock()
done = False
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background,(0,0))
    ball1.update()
    ball2.update()
    alllist.draw(screen)
    result = pygame.sprite.collide_rect(ball1, ball2)
    if result == True:
        ball1.collide()
        ball2.collide()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
    
    
