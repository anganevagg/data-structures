class Node:
	def __init__(self, data):
		self.data=data
		self.rigth=None
		self.left=None


def print_tree(root, space=0, t=0):
	count=3
	if root is None:
		return
	space+=count
	print_tree(root.rigth, space, 1)
	for x in range(count, space):
		print(" ", end="")
	if t==1:
		print("/ ", root.data)
	elif t==2:
		print("\ ", root.data)
	else:
		print(root.data)
	print_tree(root.left, space, 2)

root=Node(1)
root.left=Node(2)
root.rigth=Node(3)
root.left.left=Node(4)
root.rigth.rigth=Node(5)
root.rigth.left=Node(6)
print_tree(root)
