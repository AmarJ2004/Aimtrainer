#------[Aimtrain by Pixel Cluster]------
import pygame
import math
import random

pygame.init()

#wINDOW INFO
width = 1365
height = 710
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('AimTrain')
icon = pygame.image.load('C:\\Users\\HP\\OneDrive\\Desktop\\Projects of Programming\\Aimtrain\\aim.png')
pygame.display.set_icon(icon)

#For cursor
pygame.mouse.set_visible(False)  # hide the cursor

# Image for "manual" cursor
image = pygame.image.load('C:\\Users\\HP\\OneDrive\\Desktop\\Projects of Programming\\Aimtrain\\Scop.png').convert_alpha()
target = pygame.image.load('C:\\Users\\HP\\OneDrive\\Desktop\\Projects of Programming\\Aimtrain\\targept.png').convert_alpha()

h = 100
w = 100
image = pygame.transform.scale(image,(h,w))

black=(0,0,0)
white= (255,255,255)
Green= (67,112,65)
clock=pygame.time.Clock()

    # print cursor at mouse the current location
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = pygame.mouse.get_pos(2)[0]
    y = pygame.mouse.get_pos(2)[1]
    click = pygame.mouse.get_pressed
    
    display.fill(Green)
    display.blit(image,(x-w/2,y-h/2))
    
    
    pygame.display.update()
    clock.tick()
        
