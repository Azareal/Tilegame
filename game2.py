import pygame, sys, math
from pygame.locals import *

TILESIZE = 8
WIDTH = 50
HEIGHT = 50
tilegrid = {}
dynamic_sprite_colliders = {}

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GRAY = (195,195,195)
DARK_BROWN = (128,64,0)

textures = {
	'BLANK': 0
}

structures = {
	'road': (
	('ROAD_LEFT_LAMP','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_RIGHT_LAMP'),
	('ROAD_LEFT','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_RIGHT'),
	('ROAD_LEFT','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_RIGHT')
	),
	
	'half_road': (
	('ROAD_LEFT_LAMP','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_RIGHT_LAMP'),
	('ROAD_LEFT','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_MIDDLE','ROAD_RIGHT')
	),
	
	'medium_house': (
	('BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL'),
	('BRICK_WALL','POTTED_PLANT','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('BRICK_WALL','CARPET','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('WINDOW','CARPET','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('WINDOW','CARPET','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('BRICK_WALL','SMALL_DOOR_TOP','INNER_WALL','INNER_WALL','INNER_WALL','INNER_WALL','SMALL_DOOR_TOP','INNER_WALL','INNER_WALL','INNER_WALL','INNER_WALL','BRICK_WALL'),
	('DOOR','CARPET','CARPET','CARPET','CARPET','CARPET','CARPET','CARPET','STAIR_LEFT','STAIR_MIDDLE','STAIR_MIDDLE','BRICK_WALL'),
	('BRICK_WALL','SMALL_DOOR_BOTTOM','INNER_WALL','INNER_WALL','INNER_WALL','INNER_WALL','SMALL_DOOR_BOTTOM','INNER_WALL','INNER_WALL','INNER_WALL','INNER_WALL','BRICK_WALL'),
	('WINDOW','CARPET','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('WINDOW','CARPET','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('BRICK_WALL','POTTED_PLANT','CARPET','CARPET','CARPET','INNER_WALL','CARPET','CARPET','CARPET','CARPET','CARPET','BRICK_WALL'),
	('BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL','BRICK_WALL')
	)
}

pygame.init()
pygame.event.set_blocked(pygame.MOUSEMOTION)
window = pygame.display.set_mode((WIDTH * TILESIZE * 2, HEIGHT * TILESIZE * 2))
surface = pygame.Surface((WIDTH * TILESIZE, HEIGHT * TILESIZE))

loadTextures = [
'ROAD_LEFT_LAMP','ROAD_RIGHT_LAMP','ROAD_LEFT','ROAD_RIGHT','ROAD_MIDDLE','BUSH','GRASS','PAVEMENT','DOOR','SMALL_DOOR_TOP','SMALL_DOOR_BOTTOM','INNER_WALL','BRICK_WALL','CARPET','WINDOW','FENCE','POTTED_PLANT','STAIR_LEFT','STAIR_MIDDLE'
]

for texture in loadTextures:
	try:
		image = pygame.image.load('./textures/' + texture.lower() + '.png')
	except pygame.error as message:
		print('Unable to load texture: ' + texture.lower())
		sys.exit()
	image = image.convert()
	textures[texture] = image

def setTile(x,y,value):
	tilegrid[str(x) + ':' + str(y)] = value

def getTile(x,y):
	return tilegrid[str(x) + ':' + str(y)]

def drawTiles():
	global surface
	for key, value in tilegrid.items():
		coords = key.split(':')
		xCoord = int(coords[0]) * TILESIZE
		yCoord = int(coords[1]) * TILESIZE
		surface.blit(textures[value], (xCoord, yCoord))

def getStructure(name):
	if name not in structures:
		return False
	return structures[name]

def addStructure(name = '', x = 0, y = 0, tilemap = False):
	global surface
	if name == '' and not tilemap:
		print('No name or tilemap was provided')
		return False
	
	if not tilemap:
		tilemap = getStructure(name)
		if not tilemap:
			print('Cannot find structure ' + name)
			return False
	
	r = c = 0
	width = 1
	for row in tilemap:
		for column in row:
			setTile(x + c,y + r,column)
			c = c + 1
		r = r + 1
		if c > width:
			width = c
		c = 0
	
	return (x, y, x + width, y + r)

def addRoad(length, x = 0, y = 0):
	tilemap = getStructure('road')
	tilemap = tilemap * length
	return addStructure(tilemap = tilemap, x = x, y = y)

def addMediumHouse(x = 0, y = 0, garden = True):
	addGarden(x,y)
	addStructure('medium_house', x + 12, y)
	width = 25
	if not garden:
		width = width - 13
	return (x, y, width, 14)

def addGarden(x = 0, y = 0, width = 12, height = 14):
	global surface
	
	# Add the bushes
	for i in range(height):
		setTile(x,y + i,'BUSH')
		setTile(x + 11,y + i,'BUSH')
	
	# Add the grass
	for row in range(height):
		for column in range(9):
			setTile(x + column + 1,y + row,'GRASS')
	
	# Add the pavement
	for column in range(12):
		setTile(x + column,y + 6,'PAVEMENT')
	for i in range(height):
		setTile(x + 10,y + i,'PAVEMENT')

#def addFence(length, x, y):
#	

def mapgen():
	roadCoords = addRoad(5)
	addStructure(name = 'half_road', x = roadCoords[0], y = roadCoords[3])
	addMediumHouse(x = roadCoords[2])
	#addFence(19)

background = pygame.Surface(surface.get_size())
background.fill((255, 255, 255))
mapgen()

while True:
	surface.blit(background,(0, 0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	drawTiles()
	pygame.transform.scale2x(surface, window)
	pygame.display.update()