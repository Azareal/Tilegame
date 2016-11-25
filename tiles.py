warps = {}

def addWarpTile(special_tiles, tileX, tileY, destMap, destWarp):
	if destWarp in warps:
		destWarp = warps[destWarp]
	else:
		return False
	special_tiles[str(tileX) + ':' + str(tileY)] = WarpTile(tileX, tileY, destMap, destWarp)
	return True

class WarpTile:
	tile = (0,0)
	destMap = False
	destWarp = False
	
	def __init__(self, tileX, tileY, destMap, destWarp):
		self.tile = (tileX,tileY)
		self.destMap
		self.destWarp
	
	def activate(self):
		pass