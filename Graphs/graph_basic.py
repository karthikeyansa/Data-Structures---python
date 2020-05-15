class Graph(object):
	def __init__(self,graph = None):
		if graph == None:
			graph = {}
		self.graph = graph
	def vertices(self):
		return list(self.graph.keys())
	#def values(self):
	#	return list(self.graph.values())
	def add_vertex(self,vertex):
		if vertex not in self.graph:
			self.graph[vertex] = []
	def edges(self):
		return self.generate_edge()
	def add_edge(self,edge):
		edge = set(edge)
		(vertex1,vertex2) = tuple(edge)
		if vertex1 in self.graph:
			self.graph[vertex1].append(vertex2)
		else:
			self.graph[vertex1] = [vertex2]
	def generate_edge(self):
		edges = []
		for vertex in self.graph:
			for neighbour in self.graph[vertex]:
				if {neighbour,vertex} not in edges:
					edges.append({vertex,neighbour})
		return edges
	def __str__(self):
		res = 'vertices: '
		for vertices in self.graph:
			res+=vertices+' '
		res+='\nedges: '
		for edge in self.generate_edge():
			res+=str(edge) + ' '
		return res

if __name__  == '__main__':
	g = {
	'a' : ['c','b','d'],
	'b' : ['d','a'],
	'c' : ['a'],
	'd' : ['a','b']
	}
	graph = Graph(g)
	graph.add_vertex('e')
	graph.add_edge({'e','z'})
	print(graph.vertices())
	print(graph.edges())
	print(graph)