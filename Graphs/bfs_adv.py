#undirected_cyclic_graph
def bfs(g,s):
	vis,queue = {s},[s]
	while queue:
		u = queue.pop()
		for u in g[u]:
			if u not in vis:
				vis.add(u)
				queue.append(u)
	return vis
n,m = map(int,input().split())
g = {}
for i in range(n):
	g[i+1] = []
for _ in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)
print(bfs(g,1))