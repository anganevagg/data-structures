class Matriz:
	def __init__(self):
		self.items=[]
	def input(self, rows):
		for _ in range(rows):
			self.items.append(list(map(int, input().split())))
	def print(self):
		for i in self.items:
			print(i)
	def sum(self, matriz):
		res=[]
		for i in range(len(self.items)):
			res.append([])
			for j in range(len(self.items[i])):
				res[i].append(self.items[i][j]+matriz.items[i][j])
		return res

m=Matriz()
m.input(3)
n=Matriz()
n.input(3)
for i in m.sum(n):
	print(i)
