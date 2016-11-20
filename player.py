import pygame, entity

class Player(entity.Entity):
	noclip = False
	money = 0
	inventory = []
	
	def __init__(self, x, y):
		super(Player, self).__init__('player', x, y)
	
