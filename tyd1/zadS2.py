a = 0
b = 1
print(a/b)
for x in range(0, 200):
	c = a + b
	a = b
	b = c
	print(a/b)
