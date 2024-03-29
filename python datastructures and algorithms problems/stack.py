class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items )


s = Stack()
print(s.isEmpty())
s.push(1)
s.push('two')
s.push(4)
a = s.pop()
print(a)
print(s.peek())
print(s.size())