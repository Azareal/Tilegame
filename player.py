import pygame, entity
from inventory import *

class Player(entity.Entity):
	noclip = False
	money = 0
	inventory = False
	
	def __init__(self, x, y, colliders):
		super(Player, self).__init__('player', x, y, colliders)
		self.inventory = Inventory()
