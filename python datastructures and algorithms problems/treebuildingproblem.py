import collections 

class Node:
	def __init__(self, val= None):
		self.left = None
		self.right = None
		self.val = val


def levelorder(tree):
	if not tree:
		return 
	nodes = collections.deque([tree])
	currentcount = 1
	nextcount = 0




	while len(nodes) != 0:
		currentnode = nodes.popleft()
		currentcount -=1

		print(currentnode.val)
	

		if currentnode.left:
			print(currentnode.left.val)
			nodes.append(currentnode.left)
			nextcount +=1

		if currentnode.right:
			
			nodes.append(currentnode.right)
			nextcount +=1 
		
		if currentcount == 0:
			
			currentcount,nextcount = nextcount,currentcount

		
root = Node(1)
root.left = Node(3)
root.right= Node(2)
levelorder(root)
