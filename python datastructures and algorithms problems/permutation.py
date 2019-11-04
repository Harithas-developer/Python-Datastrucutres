def permute(s):
	out = []

	if len(s) == 1:
		out = [s]
	else:
		for i , let in enumerate(s):
			for perm in permute(s[:i] + s[i+1:]):
				out += [let+perm]
	return out

a = permute('abc')
print(a)