import pygame, math

class Player:
	image = False
	x = 0
	y = 0
	xdir = 0
	ydir = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		try:
			self.image = pygame.image.load('./sprites/player.png')
		except pygame.error as message:
			print('Unable to load sprite: ' + texture.lower())
			sys.exit()
		self.image = self.image.convert()
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def move(self, xdir = 0, ydir = 0):
		self.xdir = xdir
		self.ydir = ydir
	
	def draw(self, surface, delta):
		speed = 1 / float(delta)
		if self.xdir != 0:
			self.x += self.xdir# * speed
		if self.ydir != 0:
			self.y += self.ydir# * speed
		self.xdir = 0
		self.ydir = 0
		
		surface.blit(self.image, (int(math.floor(self.x)), int(math.floor(self.y))))
