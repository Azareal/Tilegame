import pygame, entity, items, config
from inventory import *

BASE_STATS = ['coins','gears','karma','speed_mod']

class Player(entity.Entity):
	coins = 0
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
			if item.type == items.RESOURCE:
				self.useItem(item)
			else:
				self.inventory.addItem(item)
			del tile_items[coords]
			if item.owner != 0:
				print("Stole the '" + item.name + "' item")
				self.karma -= 2
				print("Lost " + str(item.karma) + " karma")
			else:
				print("Picked up the '" + item.name + "' item")
			return True
		return False
	
	def useItem(self, item):
		if not item.consumable:
			return
		
		if item.coins > 0:
			self.coins += item.coins
			print("Gained " + str(item.coins) + " coins")
		elif item.coins < 0:
			self.coins += item.coins
			print("Lost " + str(item.coins) + " coins")
		
		if item.karma < 0:
			self.karma += item.karma
			print("Lost " + str(item.karma) + " karma")
		elif item.karma > 0:
			self.karma += item.karma
			print("Gained " + str(item.karma) + " karma")
		
		if item.gears < 0:
			self.gears += item.gears
			print("Lost " + str(item.gears) + " gears")
		elif item.gears > 0:
			self.gears += item.gears
			print("Gained " + str(item.gears) + " gears")
		
		if item.speed < 0:
			self.speed_mod += item.speed
			print("Lost " + str(item.speed) + " speed")
		elif item.speed > 0:
			self.speed_mod += item.speed
			print("Gained " + str(item.speed) + " speed")
		
		item.special_effect(self)
