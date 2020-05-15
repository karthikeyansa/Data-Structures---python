#undirected weighted cyclic graph
def prim(g,s):
	dist,vis,path = {s:0},set(),{s:0}
	while True:
		if len(vis) == len(g)-1:
			break
		mini = 1000000
		for i in dist:
			if i not in vis and dist[i]<mini:
				mini = dist[i]
				u = i
		vis.add(u)
		for v in g[u]:
			if v[0] not in vis and v[1] < dist.get(v[0],1000000):
				dist[v[0]] = v[1]
				path[v[0]] = u
	return sum(dist.values())
n,m = map(int,input().split())
g = {}
for i in range(n):
	g[i+1] = []
for _ in range(m):
	x,y,r = map(int,input().split())
	g[x].append([y,r])
	g[y].append([x,r])
print(prim(g,1))