from collections import deque
#UCG->undirected cyclic graph
def bfs(g,s):
	vis,q = {s},deque([s])
	print(s)
	while q:
		u = q.popleft()
		for v in g[u]:
			if v not in vis:
				vis.add(v)
				q.append(v)
				print(v)
def dfs(g,s):
	vis,s = {s},[s]
	print(s)
	print(g[s[-1]],'g[s[-1]]')
	while s:
		flag = 0
		for i in g[s[-1]]:
			if i not in vis:
				vis.add(i)
				s.append(i)
				flag = 1
				print(i)
				break
		if not flag:
			s.pop()

n,m=map(int,input().split(" "))
g = {}
for i in range(n):
	g[i+1]=[]
print(g)
#adding edges to directed graph
for _ in range(m):
	x,y = map(int,input().split(" "))
	g[x].append(y)
#adding edgea to undirected graph
for _ in range(m):
	x,y = map(int,input().split(" "))
	g[x].append(y)
	g[y].append(x)
#adding edges to weighted undirected graph
#r -> weight
for _ in range(m):
	x,y,r = map(int,input().split(" "))
	g[x].append([y,r])
	g[y].append([x,r])
print(g)
bfs(g,1)
dfs(g,1)