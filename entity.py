import pygame, math, config

def absoluteToTile(coord):
	return math.floor(coord / config.TILESIZE) * config.TILESIZE

class Entity:
	image = False
	x = 0
	y = 0
	tile = (0,0)
	xdir = 0
	ydir = 0
	speed = 16
	
	colliders = {}
	
	def __init__(self, name, x, y, colliders):
		self.x = x
		self.y = y
		self.tile = (absoluteToTile(x),absoluteToTile(y))
		self.colliders = colliders
		
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
	
	def setX(self,x):
		self.x = x
	
	def setY(self, y):
		self.y = y
	
	def move(self, xdir = 0, ydir = 0):
		self.xdir = xdir
		self.ydir = ydir
	
	def draw(self, surface, delta):
		dspeed = 1 / float(delta)
		if self.xdir != 0:
			nextX = self.tile[0] + self.xdir
			currentY = self.tile[1]
			if str(nextX) + ':' + str(currentY) in self.colliders and self.colliders[str(nextX) + ':' + str(currentY)]:
				self.xdir = 0
				return
			self.x += self.xdir * self.speed * dspeed
		if self.ydir != 0:
			nextY = self.tile[1] + self.ydir
			currentX = self.tile[0]
			if str(currentX) + ':' + str(nextY) in self.colliders and self.colliders[str(currentX) + ':' + str(nextY)]:
				self.ydir = 0
				return
			self.y += self.ydir * self.speed * dspeed
		self.xdir = 0
		self.ydir = 0
		
		tileX = absoluteToTile(self.x)
		tileY = absoluteToTile(self.y)
		self.tile = (tileX,tileY)
		surface.blit(self.image,(int(tileX),int(tileY)))
