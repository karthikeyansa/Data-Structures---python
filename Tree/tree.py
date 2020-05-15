class Node(object):
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):
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
	
	def printree(self):
		if self.left:
			self.left.printree()
		print(self.data)
		if self.right:
			self.right.printree()

#n = int(input('enter total number of nodes'))
#arr = [int(n) for n in input('enter elements separated by space').split()]
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.printree()





