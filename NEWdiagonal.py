import math 

def func(line, diagonal):
	line = line + 1
	diagonal = diagonal + 1
	return math.comb(line, diagonal)

print(func(7, 2))
print(func(2**100, 16))
