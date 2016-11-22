import pygame, pygame.font, math, config

#pygame.font.init()

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
	arial = False
	
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
		self.arial = pygame.font.SysFont("Arial", 10)
	
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
			nextX = self.tile[0] + (self.xdir * config.TILESIZE)
			currentY = self.tile[1]
			coords = str(nextX) + ':' + str(currentY)
			print(coords)
			if coords in self.colliders and self.colliders[coords]:
				self.xdir = 0
				print('Aaahhh!!!')
				return
			self.x += self.xdir * self.speed * dspeed
		if self.ydir != 0:
			nextY = self.tile[1] + (self.ydir * config.TILESIZE)
			currentX = self.tile[0]
			coords = str(currentX) + ':' + str(nextY)
			print(coords)
			if coords in self.colliders and self.colliders[coords]:
				self.ydir = 0
				print('Aaahhh!!!')
				return
			self.y += self.ydir * self.speed * dspeed
		self.xdir = 0
		self.ydir = 0
		
		tileX = absoluteToTile(self.x)
		tileY = absoluteToTile(self.y)
		self.tile = (tileX,tileY)
		surface.blit(self.image,(int(tileX),int(tileY)))
		
		if config.debug:
			text = self.arial.render(str(tileX) + ":" + str(tileY), False, (0,0,255))
			surface.blit(text,(2,136))
