import pygame, pygame.font, math, config

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

def absoluteToTileAbsolute(coord):
	return math.floor(coord / config.TILESIZE) * config.TILESIZE

def absoluteToTile(coord):
	return math.floor(coord / config.TILESIZE)

class Entity:
	name = "Unknown Entity"
	image = False
	x = 0
	y = 0
	tile = (0,0)
	dir = 0
	speed = 16
	
	colliders = {}
	font = False
	phantom = False
	
	def __init__(self, name, tileX, tileY, colliders):
		self.name = name
		self.x = tileX * config.TILESIZE
		self.y = tileY * config.TILESIZE
		self.tile = (tileX,tileY)
		self.colliders = colliders
		
		try:
			self.image = pygame.image.load('./sprites/' + name.lower() + '.png')
		except pygame.error as message:
			print('Unable to load sprite: ' + name.lower())
			sys.exit()
		self.image = self.image.convert()
		self.font = pygame.font.SysFont(config.font, 10)
	
	def getRawX(self):
		return self.x
	
	def getRawY(self):
		return self.y
	
	def setRawX(self,rawX):
		self.x = rawX
	
	def setRawY(self, rawY):
		self.y = rawY
	
	def getTile(self):
		return self.tile
	
	def setTile(self, tileX, tileY):
		self.tile = (tileX, tileY)
	
	def setPosition(self, tileX, tileY):
		self.x = tileX * config.TILESIZE
		self.y = tileY * config.TILESIZE
		self.tile = (tileX, tileY)
		self.dir = 0
	
	def getPosition(self):
		return self.tile
	
	def setSpeed(self, newSpeed):
		self.speed = newSpeed
	
	def getSpeed(self):
		return self.speed
	
	def move(self, dir = 0):
		self.dir = dir
	
	def draw(self, surface, delta):
		dspeed = 1 / float(delta)
		if self.dir == LEFT:
			nextX = self.tile[0] - 1
			currentY = self.tile[1]
			coords = str(nextX) + ':' + str(currentY)
			print(coords)
			if coords in self.colliders and self.colliders[coords] > 0 and not self.phantom:
				self.dir = 0
				print(coords)
				print('Aaahhh!!!')
				return
			self.x += -1 * self.speed * dspeed
		elif self.dir == RIGHT:
			nextX = self.tile[0] + 1
			currentY = self.tile[1]
			coords = str(nextX) + ':' + str(currentY)
			print(coords)
			if coords in self.colliders and self.colliders[coords] > 0 and not self.phantom:
				self.dir = 0
				print(coords)
				print('Aaahhh!!!')
				return
			self.x += 1 * self.speed * dspeed
		
		if self.dir == UP:
			nextY = self.tile[1] - 1
			currentX = self.tile[0]
			coords = str(currentX) + ':' + str(nextY)
			print(coords)
			if coords in self.colliders and self.colliders[coords] > 0 and not self.phantom:
				self.dir = 0
				print(coords)
				print('Aaahhh!!!')
				return
			self.y += -1 * self.speed * dspeed
		elif self.dir == DOWN:
			nextY = self.tile[1] + 1
			currentX = self.tile[0]
			coords = str(currentX) + ':' + str(nextY)
			print(coords)
			if coords in self.colliders and self.colliders[coords] > 0 and not self.phantom:
				self.dir = 0
				print(coords)
				print('Aaahhh!!!')
				return
			self.y += 1 * self.speed * dspeed
		self.dir = 0
		
		tileX = int(absoluteToTile(self.x))
		tileY = int(absoluteToTile(self.y))
		self.tile = (tileX,tileY)
		surface.blit(self.image,(tileX * config.TILESIZE,tileY * config.TILESIZE))
		
		if config.debug:
			text = self.font.render(str(tileX * config.TILESIZE) + ":" + str(tileY * config.TILESIZE), False, (0,0,255))
			surface.blit(text,(2,136))
			text = self.font.render(str(tileX) + ":" + str(tileY), False, (0,0,255))
			surface.blit(text,(2,146))
