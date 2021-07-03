# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:25:53 2021

@author: konan
"""
import pygame, random
from queue import Queue

BLACK = (0 ,0 ,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

seg_width = 18
seg_height = 18

seg_margin = 2
seg_head_x = 0
seg_head_y = 0

x_change = 1
y_change = 0
score = 0

class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([seg_width, seg_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x * (seg_width + seg_margin)
        self.rect.y = y * (seg_height + seg_margin)
        self.x = x
        self.y = y

pygame.init()

screen = pygame.display.set_mode([800,600])

alllist = pygame.sprite.Group()

snake_seg = Queue()
for i in range(3):
    x = i
    y = 0
    segment = Segment(x, y)
    snake_seg.put(segment)
    alllist.add(segment)
    seg_head_x = x
    seg_head_y = y
clock = pygame.time.Clock()
done = False
eat = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (-1)
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (-1)
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 1
    if eat == True:
        xa = random.randrange(40)
        ya = random.randrange(30)
        eat = False
    else:
        print("HELLO")
        old_seg = snake_seg.get()
        alllist.remove(old_seg)
    seg_head_x = seg_head_x + x_change
    seg_head_y = seg_head_y + y_change
    segment = Segment(seg_head_x, seg_head_y)
    snake_seg.put(segment)
    alllist.add(segment)
    apple = Segment(xa,ya)
    if segment.x == apple.x and segment.y == apple.y:
        score = score + 1
        pygame.display.set_caption("分數:" + str(score))
        eat = True
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED,(xa * (seg_width + seg_margin), ya * (seg_height + seg_margin),seg_width,seg_height))
    alllist.draw(screen)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
