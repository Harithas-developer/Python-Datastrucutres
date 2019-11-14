class BinaryHeap():
	def __init__(self):
		self.heapList = [0]
		self.currentsize = 0

	def percup(self,i):
		print(i)
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2 ]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2
			print(self.heapList)

	def insert(self, k):
		self.heapList.append(k)
		self.currentsize = self.currentsize+1
		print(self.currentsize)
		self.percup(self.currentsize)

	def percdown(self,i):
		while(i * 2) <= self.currentsize:
			mc = self.minchild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minchild(self,i):
		if i * 2 +1 > self.currentsize:
			return i *2 
		else:
			if self.heapList[i * 2] < self.heapList[i*2+1]:
				return i*2
			else:
				return i * 2 +1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentsize]
		self.currentsize = self.currentsize-1
		self.heapList.pop()
		self.percdown(1)
		return retval


a = BinaryHeap()
a.insert(2)
a.insert(5)
b = a.delMin()
print(b)
