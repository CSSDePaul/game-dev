import random, pygame, sys
from pygame.locals import *
import taxhole

GAME_TITLE = 'Taxes'
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)


def runGame():
	global FPSCLOCK, DISPLAYSURF
	#setup
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption(GAME_TITLE)
	
	#initiate variables
	mousex = 0 # used to store x coordinate of mouse event
	mousey = 0 # used to store y coordinate of mouse event
	stillPlaying = True
	score = 0
	holes = taxhole.initializeHoles()
	
	while stillPlaying: # main game loop
		#-------UPDATE VARIABLES-------
		for hole in holes:
			hole.update()
			
		#-------CHECK FOR POINTS-------
		for hole in holes:	
			if hole.checkMouseover(mousex, mousey):
				score += 1
				break
		
		#-------DRAW STUFF--------
		DISPLAYSURF.fill(BGCOLOR)
		for hole in holes:
			hole.draw(DISPLAYSURF)
		
		#-------HANDLE EVENTS-------------
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			
		#--------FINAL------------
		pygame.display.update() #redraw the screen
		FPSCLOCK.tick(FPS) #wait for clock tick

def main():
	runGame()
	
if __name__ == "__main__":
	main()
