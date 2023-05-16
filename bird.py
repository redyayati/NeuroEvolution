from nn import NeuralNetwork
import math
from pygame import gfxdraw
from variables import *
class Bird() :
        def __init__(self , brain = None) : 
            self.x = 64
            self.y = height/2
            self.vel = 0
            self.size = 15
            self.fitness = 0 
            self.gravity = .8
            self.score = 0
            if brain : self.brain = brain.copy() 
            else : self.brain = NeuralNetwork(5,8,2)
        def update(self):
            self.score += 1
            self.vel += self.gravity
            self.y += self.vel
        def offscreen (self) : 
            return self.y < 0 or self.y > height
        def jump(self):
            self.vel = -8
            
        def think(self , walls):
            closest_d = math.inf
            closest_wall = None
            for wall in walls : 
                d = wall.x + wall.thickness - self.x
                if d < closest_d and d > 0 : 
                    closest_d = d 
                    closest_wall = wall
            birdY = self.y / height
            wallX = closest_wall.x /width
            # pg.draw.line(screen , (200,200,200) , (self.x,self.y),(closest_wall.x+closest_wall.thickness,closest_wall.topHeight),1)
            upperGapY = closest_wall.topHeight  / height
            lowerGapY = (closest_wall.topHeight + closest_wall.gap) / height
            birdVel = self.vel / 10
            inputs = [birdY ,  upperGapY,lowerGapY ,wallX ,birdVel ]
            out = self.brain.predict(inputs)
            if out[0] > out[1] : 
                self.jump()
        def mutate(self): 
            self.brain.mutate(.1)
        def draw(self):
            # pg.draw.circle(screen,(100,100,100),(int(self.x),int(self.y)),self.size,1)
            # pg.draw.rect(screen,(250,150,150) , (int(self.x)-self.size, int(self.y)-self.size, 2*self.size , 2*self.size))
            gfxdraw.filled_circle(screen,int(self.x),int(self.y),self.size,(180,130,160,90))
            gfxdraw.circle(screen,int(self.x),int(self.y),self.size,(210,210,210,150))
        def crashed(self, wall) : 
            if self.y < wall.topHeight or self.y > wall.topHeight + wall.gap : 
                if self.x > wall.x and self.x < wall.x + wall.thickness : 
                    return True 
            else : return False
        def crashedOriginal(self, wall) : 
            if wall.x - self.size <= self.x <= wall.x + wall.thickness+ self.size : 
                if self.y <= wall.topHeight + self.size or self.y >= wall.topHeight + wall.gap - self.size: 
                    return True 
            else : return False