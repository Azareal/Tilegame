import pygame, pygame.font, math, config

#pygame.font.init()

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

def absoluteToTileAbsolute(coord):
	return math.floor(coord / config.TILESIZE) * config.TILESIZE

def absoluteToTile(coord):
	return math.floor(coord / config.TILESIZE)

class Entity:
	image = False
	x = 0
	y = 0
	tile = (0,0)
	dir = 0
	speed = 16
	
	colliders = {}
	arial = False
	
	def __init__(self, name, x, y, colliders):
		self.x = x
		self.y = y
		self.tile = (int(absoluteToTile(x)),int(absoluteToTile(y)))
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
	
	def move(self, dir = 0):
		self.dir = dir
	
	def draw(self, surface, delta):
		dspeed = 1 / float(delta)
		if self.dir == LEFT:
			nextX = self.tile[0] - 1
			currentY = self.tile[1]
			coords = str(nextX) + ':' + str(currentY)
			print(coords)
			if coords in self.colliders and self.colliders[coords]:
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
			if coords in self.colliders and self.colliders[coords]:
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
			if coords in self.colliders and self.colliders[coords]:
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
			if coords in self.colliders and self.colliders[coords]:
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
			text = self.arial.render(str(tileX * config.TILESIZE) + ":" + str(tileY * config.TILESIZE), False, (0,0,255))
			surface.blit(text,(2,136))
			text = self.arial.render(str(tileX) + ":" + str(tileY), False, (0,0,255))
			surface.blit(text,(2,146))
