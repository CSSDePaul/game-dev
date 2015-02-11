import math
import pygame
from tax_constants import *
import random

def initializeHoles():
	holes = set()
	for i in range(5):
		holes.add(randomHole())
	return holes

def randomHole():
	x = random.randint(0, WINDOWWIDTH)
	y = random.randint(0, WINDOWHEIGHT)
	r = random.randint(5,15)
	a = random.uniform(0, 2*math.pi)
	s = random.randint(5,15)
	return Hole(x, y, r, a, s)
	
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
		self.checkOffScreen()
		
	def checkOffScreen(self):
		if self.xpos < 0:
			self.xpos = WINDOWWIDTH
		if self.ypos < 0:
			self.ypos = WINDOWHEIGHT
		if self.xpos > WINDOWWIDTH:
			self.xpos = 0
		if self.ypos > WINDOWHEIGHT:
			self.ypos = 0
			
		
	def randomizeTrajectory():
		pass 
		
	def draw(self, displaysurf):
		pygame.draw.circle(displaysurf, BLACK, (self.xpos, self.ypos), self.radius, 0)
		
	def checkMouseover(self, x, y):
		pass
	


