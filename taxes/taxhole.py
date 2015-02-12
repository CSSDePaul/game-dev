import math
import pygame
from tax_constants import *
import random

def initializeHoles(difficulty=3):
	holes = set()
	for i in range(difficulty):
		holes.add(randomHole(difficulty))
	return holes

def randomHole(difficulty):
	x = random.randint(0, WINDOWWIDTH)
	y = random.randint(0, WINDOWHEIGHT)
	r = random.randint( TAXES_MIN_RADIUS_BASE+TAXES_MIN_RADIUS_FACTOR*difficulty, 
						TAXES_MAX_RADIUS_BASE+TAXES_MAX_RADIUS_FACTOR*difficulty)
	a = random.uniform(0, 2*math.pi)
	s = random.randint(TAXES_MIN_SPEED_BASE+difficulty, TAXES_MAX_SPEED_BASE+difficulty)
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
		self.randomizeTrajectory()


	def checkOffScreen(self):
		if self.xpos < 0:
			self.xpos = WINDOWWIDTH
		if self.ypos < 0:
			self.ypos = WINDOWHEIGHT
		if self.xpos > WINDOWWIDTH:
			self.xpos = 0
		if self.ypos > WINDOWHEIGHT:
			self.ypos = 0
			
		
	def randomizeTrajectory(self):
		if random.uniform(0,1) < TAXES_BOUNCE_PROBABILITY:
			self.angle = random.uniform(0, 2*math.pi)
		
	def draw(self, displaysurf):
		pygame.draw.circle(displaysurf, BLACK, (self.xpos, self.ypos), self.radius, 0)
		
	def checkMouseover(self, x, y):
		return (self.xpos - self.radius <= x <= self.xpos + self.radius) and \
		(self.ypos - self.radius <= y <= self.ypos + self.radius)
		
		
	
