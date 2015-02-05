import math
import pygame

def initializeHoles():
	holes = set()
	holes.add(Hole(200,200, 10, 0, 10))
	return holes

def randomHole():
	pass
	
BLACK = (0,0,0)

class Hole:
	
	def __init__(self, xpos, ypos, radius, angle, speed):
		self.xpos = xpos
		self.ypos = ypos
		self.radius = radius
		self.angle = angle
		self.speed = speed
	
	def update(self):
		self.xpos += int(math.cos(self.angle)*self.speed)
		self.ypos += int(math.sin(self.angle)*self.speed)
		self.checkBounce()
		
	def checkOffScreen(self):
		pass
		
	def randomizeTrajectory():
		pass
		
	def draw(self, displaysurf):
		pygame.draw.circle(displaysurf, BLACK, (self.xpos, self.ypos), self.radius, 0)
		
	def checkMouseover(self, x, y):
		pass
	


