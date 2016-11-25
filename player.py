import pygame, entity, config
from inventory import *

class Player(entity.Entity):
	money = 0
	gears = 0
	karma = 0
	inventory = False
	
	def __init__(self, tileX, tileY, colliders):
		super(Player, self).__init__('player', tileX, tileY, colliders)
		self.inventory = Inventory()
	
	def pickup(self, tile_items):
		coords = str(self.tile[0]) + ':' + str(self.tile[1])
		if coords in tile_items and tile_items[coords].pickup:
			item = tile_items[coords]
			self.inventory.addItem(item)
			del tile_items[coords]
			#if config.debug:
			print("Picked up the '" + item.name + "' item")
			return True
		return False
