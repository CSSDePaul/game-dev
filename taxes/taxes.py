import random, pygame, sys
from pygame.locals import *
import taxhole
from tax_constants import *


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
				print score
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
