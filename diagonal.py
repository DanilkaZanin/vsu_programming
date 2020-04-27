
import time

def f():
	time.sleep(2)


def diagonal(level, num):
	if not num:
		return level
	values = [[1], [1, 1]]
	for i in range(2, level + 1):
		row = []
		for j in range(len(values[i-1]) - 1):
			row.append(values[i-1][j] + values[i-1][j+1])
		values.append([1, *row, 1])
	return sum([i[num] for i in values [num:]])

print(diagonal(7, 0))
print(diagonal(7, 1))
print(diagonal(7, 2))
print(diagonal(20, 3))
print(diagonal(20, 4))

t1 = time.time()
f() 
print(time.time() - t1)
