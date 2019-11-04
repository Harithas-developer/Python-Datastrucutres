# # class Node(object):
# # 	def __init__(self , value):
# # 		self.value = value
# # 		self.nextnode = None


# # a = Node(1)
# # b = Node(2)
# # c = Node(3)

# # print(a.value)
# # print(b.value)
# # a.nextnode = b
# # b.nextnode = c

# # print(a.nextnode.value)



# Dobuly linked list
class Node(object):
	"""docstring for ClassName"""
	def __init__(self, value):
		self.value = value
		self.nextnode = None
		self.prevnode = None


a = Node(1)
b = Node(2)
c=Node(3)
d=Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

b.prevnode = a
c.prevnode = b
d.prevnode = c

print(a.nextnode.value,d.prevnode.value)