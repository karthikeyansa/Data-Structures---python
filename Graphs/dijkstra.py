import heapq
#directed weighted cyclic graph
def dij(g,start,end):
	heap=[(0,start)]
	visited = set()
	while heap:
		(cost,u)=heapq.heappop(heap)
		if u not in visited:
			visited.add(u)
		if u == end:
			return cost
		for v,c in g[u]:
			if v not in visited:
				next = cost+c
				heapq.heappush(heap,(next,v))
	return -1

n,m = map(int,input().split())
g = {}
for i in range(n):
	g[i+1] = []
for _ in range(m):
	x,y,r = map(int,input().split())
	g[x].append([y,r])
print(dij(g,1,4)) 