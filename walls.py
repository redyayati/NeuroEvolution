import random
import pygame as pg
from variables import *

class Wall() : 
    def __init__(self, ) : 
        self.gap = 120
        self.x = width
        self.thickness = 60
        # self.topHeight = random.randint(0,height-self.gap)
        self.topHeight = random.uniform(height / 6, 3 / 4 * height)
    def update(self) : 
        self.x -= 6
    def offscreen(self) : 
        if self.x < -self.thickness : return True
        else : return False
    def draw(self) : 
        topLength = self.topHeight
        botLength = height - (topLength + self.gap)
        yval = topLength+self.gap
        pg.draw.rect(screen,(150,150,100), (self.x,0,self.thickness, topLength))
        pg.draw.rect(screen,(150,150,100), (self.x,yval,self.thickness,botLength))
