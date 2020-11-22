class Node(object):
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

'''	def insert(self,data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			if data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
'''
	def printree(self):
		if self.left:
			self.left.printree()
		print(self.data)
		if self.right:
			self.right.printree()
			
def lca(root,n1,n2):
	if root is None:
		return None
	if root.data == n1 or root.data == n2:
		return root.data
	l_lca = lca(root.left,n1,n2)
	r_lca = lca(root.right,n1,n2)
	if l_lca and r_lca:
		return root.data
	return l_lca if l_lca is not None else r_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

	

#n = int(input('enter total number of nodes'))
#arr = [int(n) for n in input('enter elements separated by space').split()]
root.printree()
print(lca(root,4,5)) 
# 2
