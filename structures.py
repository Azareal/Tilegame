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

structure_colliders = ['BRICK_WALL','INNER_WALL']

def door_control(self, tile):
	# Lock shops at night? Or have buildings which are only open on certain days?
	pass
structure_special_colliders = {'DOOR': door_control}