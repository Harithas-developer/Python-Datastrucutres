def arrpair(arr, k):
	if len(arr)<2:
		return False

	seen = set()
	output = set()

	for num in arr:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add((min(num ,target), max(num,target)))
	print(output)
	print(seen)

arrpair([1,3,2,2] ,4)