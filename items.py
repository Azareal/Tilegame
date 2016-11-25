import pygame, config

MISC = 0
BAG = 1
STATS = 2
RESOURCE = 3
FURNITURE = 4

class Item:
	image = False
	name = ""
	desc = ""
	type = 0
	consumable = False
	coins = 0
	gears = 0
	karma = 0
	speed = 0
	event = 0
	owner = 0
	
	def __init__(self, name, imgname, desc, type = 0, consumable = False):
		self.name = name
		self.type = type
		self.consumable = consumable
		
		try:
			self.image = pygame.image.load('./items/' + imgname.lower() + '.png')
		except pygame.error as message:
			print('Unable to load item image: ' + imgname.lower())
			sys.exit()
		self.image = self.image.convert_alpha()
	
	def special_effect(self, player):
		pass

class TileItem(Item):
	pickup = True
	
	def __init__(self, name, imgname, desc, type = 0, consumable = False, pickup = True):
		super(TileItem, self).__init__(name, imgname, desc, type, consumable)
		self.pickup = pickup
	
	def getItem(self):
		return super(TileItem, self)
	
	def draw(self, surface, tileX, tileY):
		surface.blit(self.image,(tileX * config.TILESIZE,tileY * config.TILESIZE))

class HiddenTileItem(TileItem):
	def draw(self, surface, tileX, tileY):
		pass
