class Node(object):
	"""docstring for ClassName"""
	def __init__(self, value):
		
		self.value = value
		self.nextnode = None

def reverse(head):
	current  = head
	nextnode = None
	previous = None

	while current:
		nextnode = current.nextnode
		
		current.nextnode = previous
		
		previous = current
		
		current = nextnode
		
	return previous


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.nextnode.value)
print(b.nextnode.value)

reverse(a)

print(c.nextnode.value)
print(b.nextnode.value)

