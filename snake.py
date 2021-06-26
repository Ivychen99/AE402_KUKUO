# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:25:53 2021

@author: konan
"""
import pygame
from queue import Queue

BLACK = (0 ,0 ,0)
WHITE = (255, 255, 255)

seg_width = 15
seg_height = 15

seg_margin = 3
seg_head_x = 0
seg_head_y = 0

x_change = seg_width + seg_margin
y_change = 0

class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([seg_width, seg_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()

screen = pygame.display.set_mode([800,600])

alllist = pygame.sprite.Group()

snake_seg = Queue()
for i in range(3):
    x = 0 + (seg_width + seg_margin) *i
    y = 30
    segment = Segment(x, y)
    snake_seg.put(segment)
    alllist.add(segment)
    seg_head_x = x
    seg_head_y = y
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (seg_width + seg_margin) *(-1)
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (seg_width + seg_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (seg_width + seg_margin) *(-1)
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (seg_width + seg_margin) 
    old_seg = snake_seg.get()
    alllist.remove(old_seg)
    seg_head_x = seg_head_x + x_change
    seg_head_y = seg_head_y + y_change
    segment = Segment(seg_head_x, seg_head_y)
    snake_seg.put(segment)
    alllist.add(segment)
    screen.fill(BLACK)
    alllist.draw(screen)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
