import pygame, math, config

def absoluteToTile(coord):
	return math.floor(coord / config.TILESIZE) * config.TILESIZE

class Entity:
	image = False
	x = 0
	y = 0
	xdir = 0
	ydir = 0
	
	def __init__(self, name, x, y):
		self.x = x
		self.y = y
		
		try:
			self.image = pygame.image.load('./sprites/' + name.lower() + '.png')
		except pygame.error as message:
			print('Unable to load sprite: ' + name.lower())
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
		
		surface.blit(self.image, (int(math.floor(absoluteToTile(self.x))), int(math.floor(absoluteToTile(self.y)))))
