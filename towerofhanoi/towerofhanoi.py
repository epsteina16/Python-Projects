import pygame

screen = pygame.display.set_mode((640,480))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,200,200)
white = (255,255,255)
black = (0,0,0)

screen.fill(white)

pygame.draw.line(screen, black, (60,480), (60,240))
pygame.draw.line(screen, black, (120,480), (120,240))
pygame.draw.line(screen, black, (180,480), (180,240))

pygame.draw.rect(screen, black, (40,240,40,240), 0)
pygame.display.update()

def move(n, start, middle, finish):
    if n >= 1:
        move(n - 1, start, finish, middle)
        #move first 4 in stack to the middle
        if start:
            finish.append(start.pop())
	    
	    lengthstart = len(start)
	    heightstart = float(lengthstart) * 48
	    startrec = 480 - heightstart
	    heightmiddle = len(middle) * 48
	    middlerec = 480 - heightmiddle
	    heightfinish = len(finish) * 48
	    finishrec = 480 - heightfinish
	    pygame.draw.rec(screen,black,(40,startrec,40,heightstart),0)
	    pygame.draw.rec(screen,black,(100,middlerec,40,heightmiddle),0)
	    pygame.draw.rec(screen,black,(160,finishrec,40,heightfinish),0)
    
  	    pygame.display.update()
            
	    #move largest disk to finish
        move(n - 1, middle, start, finish)
        #move stack to finish
n = 5
#n is height of tower
topstart = [5,4,3,2,1]
topmiddle = []
topfinish = []
move(len(topstart), topstart, topmiddle, topfinish)

#print topstart, topmiddle, topfinish



