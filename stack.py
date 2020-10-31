class Stack_end:
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return self.items==[]
	def push(self, item):
		self.items.insert(0, item)
	def pop(self):
		self.items.pop(0)
	def print(self):
		print(self.items)

st=Stack_end()
print("vacio", st.is_empty())
st.push(0)
st.push(1)
st.print()
print("vacio", st.is_empty())
st.pop()
st.print()

class Stack_start(Stack_end):
	def push(self, item):
		self.items.append(item)
	def pop(self):
		self.items.pop()

ste=Stack_start()
ste.print()
ste.push(4)
ste.push(3)
ste.print()
