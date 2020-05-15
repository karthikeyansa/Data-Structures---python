#undirected_cyclic_graph
def dfs(g,s):
	vis,stack = {s},[]
	stack.append(s)
	while stack:
		u = stack.pop()
		for u in g[u]:
			if u not in vis:
				vis.add(u)
				stack.append(u)
	return vis
n,m = map(int,input().split())
g = {}
for i in range(n):
	g[i+1] = []
for _ in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)
print(dfs(g,1))