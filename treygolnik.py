def otv(a, b, c):
	return a + b > c and a + c > b and b + c > a

print(otv(3, 3, 3))
print(otv(1, 1, 3))
