# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:25:53 2021

@author: konan
"""
import pygame, random, math,time

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)



class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    direction = 0
    speed = 0
    def __init__(self,sp,srx,sry,R, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([R*2,R*2])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,color,(R,R),R,0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx,sry)
        self.direction = random.randint(20,70)
        
        
    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed*math.cos(radian)
        self.dy = self.speed*math.sin(radian)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <=0 or self.rect.right >=screen.get_width()):
            self.direction  = 180 - self.direction
        elif(self.rect.top <= 0 ):
            self.direction = 360 - self.direction
        if(self.rect.bottom >= screen.get_height()):
            return True
        else:
            return False
    def collide(self):
         self.direction = 360 - self.direction
   
class Brick(pygame.sprite.Sprite):
    def __init__(self,color,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38, 13])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pad.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width) / 2)
        self.rect.y = screen.get_height() - self.rect.height - 20
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 25
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width
            
def gameover(message):
    global done
    text = font1.render(message, 1, (255,0,255))
    screen.blit(text,(screen.get_width()/2 - 125, screen.get_height()/2-20))
    #pygame.display.flip()
    #time.sleep(2)
    #done = True
pygame.init()


screen = pygame.display.set_mode((400,300))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

score = 0
msgstr = "Click to start the game."
font = pygame.font.Font(None,30)
font1 = pygame.font.Font(None,32)

alllist = pygame.sprite.Group()
bricks = pygame.sprite.Group()
ball = Ball(10,300,350,10,RED)
alllist.add(ball)
pad = Pad()
alllist.add(pad)
for row  in range(0,4):
    for col in range(0,15):
        if row == 0 or row ==1:
            brick = Brick((0,255,0),col * 40 +1, row *15 + 1)
        if row == 2 or row ==3:
            brick = Brick(BLUE,col * 40 + 1, row * 15 +1)
        bricks.add(brick)
        alllist.add(brick)

playing = False
clock = pygame.time.Clock()
done = False
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        playing = True
    if playing == True:
        screen.blit(background,(0,0))
        fail = ball.update()
        if fail:
            gameover("Lose. Please play again.")
        pad.update()
        
        hitpad = pygame.sprite.collide_rect(ball, pad)
        if hitpad == True:
            ball.collide()
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)
        if len(hitbrick)>0:
            score += len(hitbrick)
            ball.collide()
            if len(bricks) == 0:
                gameover("Mission completed.")
                
        alllist.draw(screen)
        msgstr = "Score:"+str(score)
    msg = font.render(msgstr,1,(255,0,255))
    screen.blit(msg,(0,screen.get_height()-20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
    
    
