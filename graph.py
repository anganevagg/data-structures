class Graph:
	def __init__(self, size):
		self.adj=[]
		self.size=size
		for i in range(1, size+1):
			self.adj.append([0 for i in range(size)])
	def add_edge(self, orig, dest):
		if orig>self.size or dest>self.size or orig<0 or dest<0:
			print(f"Bad edge to create in ({orig}, {dest})")
		else:
			self.adj[orig-1][dest-1]=1
			self.adj[dest-1][orig-1]=1
	def remove_edge(self, orig, dest):
		if orig>self.size or dest>self.size or orig<0 or dest<0:
			print(f"Bad edge to remove in ({orig}, {dest})")
		else:
			self.adj[orig-1][dest-1]=0
			self.adj[dest-1][orig-1]=0
	def print(self):
		for i in self.adj:
			print("")
			for j in i:
				print("{:2} ".format(j), end="")
		print("")

# Test
gr=Graph(3)
gr.add_edge(1,1)
gr.add_edge(1,2)
gr.add_edge(2,2)
gr.print()
gr.remove_edge(1,1)
gr.print()
