def helper(b):
    c = [1, *b]
    for i in range(1, len(c) - 1):
        c[i] += c[i + 1]
    return c

def diagonal(level, num):
	if not num:
		return level
	b = []
	values = []
	for i in range(level+1):
		b = helper(b)
		values.append(b)
	return sum([values[i][-(num+1)] for i in range(num, len(values))])

print(diagonal(7, 0))
print(diagonal(7, 1))
print(diagonal(7, 2))
print(diagonal(20, 3))
print(diagonal(20, 4))