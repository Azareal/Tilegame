class Inventory:
	items = []
	maxSize = 20
	
	# Insert an item at a specific index
	def insertItem(self, index, item):
		if len(items) >= self.maxSize:
			return False
		items.insert(index,item)
		return True
	
	# Insert an item at the end of the item list
	def addItem(self, item):
		if len(items) >= self.maxSize:
			return False
		items.append(item)
		return True
	
	def removeItem(self, item):
		items.remove(item)
	
	def popItem(self):
		return items.pop()
	
	def getItem(self, index):
		try:
			item = items[index]
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
		return len(items) > self.maxSize
	
	def setMaxSize(self, maxSize):
		self.maxSize = maxSize
	
	def getMaxSize(self):
		return self.maxSize
	
	def length(self):
		return len(items)
