def c(n, k):
	if 0 <= k <= n:
		n = n + 1
		k = k + 1
		nn = 1
		kk = 1
		for t in range(1, min(k, n - k) + 1):
			nn *= n
			kk *= t
			n -=1
		return nn//kk
	else:
		return 0

print(c(7, 2))
print(c(2**100, 16))
