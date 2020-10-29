import pygame,sys
from pygame.locals import *
pygame.init()
#set up window
size=(600,300)
form=pygame.display.set_mode(size)
white=(255,255,255)
catimg=pygame.image.load('cat.png')
x=10
y=10
p=(x,y)
while True:
                form.fill(white)
                form.blit(catimg,p)
                for e in pygame.event.get():
                                if e.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                pygame.display.update()
