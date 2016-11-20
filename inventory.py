class Item:
	name = ""

class Inventory:
	items = []
	
	def insertItem(self, index, item):
		items.insert(index,item)
	
	def addItem(self, item):
		items.append(item)
	
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
	
	def length(self):
		return len(items)
