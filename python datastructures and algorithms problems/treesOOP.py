class BinaryTree(object):

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newnode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newnode)
		else:
			t = BinaryTree(newnode)
			print(t.getroot())
			print(self.leftChild.getroot())
			t.leftChild = self.leftChild
			print(t.leftChild.getroot())
			self.leftChild = t
			print(self.leftChild.getroot())
			print(t.leftChild.getroot())


	def insertRight(self,newnode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newnode)
		else:
			t = BinaryTree(newnode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeft(self):
		return self.leftChild

	def getright(self):
		return self.rightChild
		
	def setrootval(self,val):
		self.key = val
	def getroot(self):
		return self.key


r = BinaryTree('a')
r.insertLeft('b')
r.insertLeft('c')
print(r.getLeft().getroot())
