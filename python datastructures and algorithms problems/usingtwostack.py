class Queuestack(object):
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enque(self,item):
		self.instack.append(item)

	def deque(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()


a = Queuestack()
a.enque(1)
a.enque(2)
print(a.deque())
