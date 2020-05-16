class Node(object):
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.hd = 0 #horizontal distance
	
	def insert(self,data):
		if self.data < data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		elif self.data > data:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)
		else:
			self.data = data
	
	def printree(self,root):
		if root.left:
			self.left.printree(root.left)
		print(self.data)
		if root.right:
			self.right.printree(root.right)
	
	def minval(node):
		cur = node
		while cur.left is not None:
			cur = cur.left
		return cur
	
	def delete(self,root,key):
		if root is None:
			return root
		if key < root.data:
			root.left = self.delete(root.left,key)
		if key > root.data:
			root.right = self.delete(root.right,key)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			if root.right is None:
				temp = root.left
				root = None
				return temp
			temp = minval(root.right)
			root.key = temp.key
			root.right = delete(root.right,temp.key)
		return root		
	
	def depth(self,root):
			if root is None:
				return 0
			else:
				dl = self.depth(root.left)
				dr = self.depth(root.right)
				if dl > dr:
					return 1+dl
				else:
					return 1+dr

	def search(self,root,key):
		if root is None:
			return False
		if root.data == key:
			return True
		if root.data < key:
			return self.search(root.right,key)
		return self.search(root.left,key)

	def binary(self,root):
		if root is None:
			return True
		if root.left is None and root.right is None:
			return True
		if root.left is not None and root.right is not None:
			return self.binary(root.left) and self.binary(root.right)
		else:
			return False

	def inorder(self,root):
		if root:
			self.inorder(root.left)
			print(root.data,end='')
			self.inorder(root.right)
	
	def postorder(self,root):
		if root:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.data,end='')
	
	def preorder(self,root):
		if root:
			print(root.data,end='')
			self.preorder(root.left)
			self.preorder(root.right)
		
	def topview(self,root):
		if root is None:
			return None
		q = []
		m = dict()
		hd = 0
		root.hd = hd
		q.append(root)
		while len(q):
			root = q[0]
			hd = root.hd

			if hd not in m:
				m[hd] = root.data
				if root.left:
					root.left.hd = hd -1
					q.append(root.left)
				if root.right:
					root.right.hd = hd+1
					q.append(root.right)
			q.pop(0)
		for i in sorted(m):
			print(m[i],end='')
	
if __name__ == '__main__':
	n = int(input())
	arr = [int(n) for n in input().split()]
	root = Node(arr[0])
	arr= arr[1:]
	for i in arr:
		root.insert(i)
	root.printree(root)
	print('top')
	root.topview(root)
	print()
	print('depth')
	print(root.depth(root))
	print()
	print('search')
	print(root.search(root,7))
	print()
	print('bst')
	print(root.binary(root))
	print()
	print('delete')
	root = root.delete(root,6)
	root.printree(root)
	print('inorder')
	root.inorder(root)
	print()
	print('preorder')
	root.preorder(root)
	print()
	print('postorder')
	root.postorder(root)
	print()
