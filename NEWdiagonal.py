import math 

def func(line, diagonal):
	return math.comb(line + 1, diagonal + 1)

print(func(7, 2))
print(func(2**100, 16))
