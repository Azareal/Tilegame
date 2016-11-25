class Inventory:
	items = []
	maxSize = 20
	
	# Insert an item at a specific index
	def insertItem(self, index, item):
		if len(self.items) >= self.maxSize:
			return False
		self.items.insert(index,item)
		return True
	
	# Insert an item at the end of the item list
	def addItem(self, item):
		if len(self.items) >= self.maxSize:
			return False
		self.items.append(item)
		return True
	
	def removeItem(self, item):
		self.items.remove(item)
	
	def popItem(self):
		return self.items.pop()
	
	def getItem(self, index):
		try:
			item = self.items[index]
		except:
			return False
		return item
	
	def hasItem(self, item):
		return item in self.items
	
	# Find and return the first occurence of an item in the list
	def findItem(self, name):
		for item in self.items:
			if item.name == name:
				return item
				
		return False
	
	def overcapacity(self):
		return len(self.items) > self.maxSize
	
	def setMaxSize(self, maxSize):
		self.maxSize = maxSize
	
	def getMaxSize(self):
		return self.maxSize
	
	def length(self):
		return len(self.items)
