n,m = map(int,input().split())
graph = {}
visited = {}
stack = []
for i in range(n):
	graph[i+1] = []
	visited[i+1] = False
for _ in range(m):
	x,y = map(int,input().split())
	graph[x].append(y)
print(graph)
print(visited)
def topo(v):
	if not visited[v]:
		visited[v] = True
		for i in graph[v]:
			topo(i)
		stack.insert(0,v)
for v in visited:
	topo(v)
print(stack)