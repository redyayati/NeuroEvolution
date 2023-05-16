import pygame as pg 
from bird import Bird
from ga import *
from variables import *
from walls import Wall
pg.init()
pg.display.set_caption('Title of window')
clock = pg.time.Clock() 
running  = True

base_font = pg.font.SysFont('consolas', 50)
textColor = (50,150,150)

for i in range(total) : 
    birds.append(Bird())
counter = 0 
walls = []
t = 0
n = 30
numGen = 0
show = True
timeLapsed = 0

while running : 
    screen.fill((0,0,0))
    for i in range(n) : 
        if counter%75 == 0 : 
            walls.append(Wall())
        counter += 1
        for wall in walls : 
            wall.update()
            for i in range(len(birds)-1,-1,-1) : 
                if birds[i].crashed(wall) : 
                    savedBirds.append(birds.pop(i))
        
        for i in range(len(birds)-1,-1,-1) : 
            if birds[i].offscreen() : 
                savedBirds.append(birds.pop(i))
        for wall in walls : 
            if wall.offscreen() : 
                walls.remove(wall)
        for bird in birds : 
            bird.think(walls)   
            bird.update()
            
        if len(birds) == 0 : 
            print("numGen : " ,numGen , " and time lapsed : ", counter)
            counter = 0
            nextGeneration()
            numGen += 1
            walls = []
    #Drawing stuff 
    if show : 
        for bird in birds : bird.draw()
        for wall in walls : wall.draw()
    
    
    text = base_font.render("Time :  " + str(counter) ,True,textColor)
    screen.blit(text,(10,30))
    
    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False  
            if event.key == pg.K_UP : 
                n += 2
                if n >= 30 : n = 30
                print(n)
            if event.key == pg.K_DOWN : 
                n -= 2
                if  n <= 0 : n = 1
                print(n)
            if event.key == pg.K_s : 
                show = True
            if event.key == pg.K_d : 
                show = False
    pg.display.flip()
    clock.tick(60)
pg.quit()
