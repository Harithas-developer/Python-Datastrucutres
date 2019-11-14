class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight

	def getConnection(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr] 

	def __str__(self):
		return str(self.id) + ' connected to : ' + str([x.id for x in self.connectedTo])


 class Graph:
 			"""docstring for """
 			def __init__(self):
 				self.vertList = {}
 				self.numVertices = 0

 			def addVertex(self,key):
 				self.numVertices += 1
 						