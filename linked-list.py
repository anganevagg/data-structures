class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

class Linked_list:
	def __init__(self):
		self.head=None
	def add_start(self, data):
		self.head=Node(data=data, next=self.head)
	def add_end(self, data):
		if not self.head:
			self.head=Node(data=data)
			return
		curr=self.head
		while curr.next:
			curr=curr.next
		curr.next=Node(data=data)
	def is_empty(self):
		return self.head==None
	def delete_node(self, key):
		curr=self.head
		prev=None
		while curr and curr.data!=key:
			prev=curr
			curr=curr.next
		if prev is None:
			self.head
		elif curr:
			prev.next=curr.next
			curr.next=None
	def get_last_node(Node):
		temp=self.head
		while temp.next is not None:
			temp=temp.next
		return temp.data
	def print(self):
		node=self.head
		while node!=None:
			print(node.data,end="=>")
			node=node.next
		print("")

link=Linked_list()
print("vacio: ", link.is_empty())
link.add_end(3)
link.add_end(2)
link.add_start(4)
link.print()
print("vacio: ", link.is_empty())
link.delete_node(3)
link.print()
