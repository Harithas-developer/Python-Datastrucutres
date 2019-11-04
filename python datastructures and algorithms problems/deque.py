class Deque:

	def __init__(self):
		self.item = []

	def isEmpty(self):
		return self.item == []

	def addrear(self,items):
		self.item.insert(0,items)

	def addfront(self,items):
		self.item.append(items)

	def rear(self):
		return self.item.pop(0)

	def front(self):
		return self.item.pop()

	def size(self):
		return len(item)

a = Deque()
a.addfront('hello')
a.addrear('world')
print(a.rear() + " " +a.front())
