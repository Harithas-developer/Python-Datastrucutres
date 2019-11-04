def largesum(arr):
	if len(arr) == 0:
		return 0

	max_sum = current_sum = arr[0]

	for num in arr[1:]:
		current_sum = max(current_sum+num, num)
		max_sum = max(current_sum,max_sum)

	return max_sum

arr = [1,2,3,4,5]
b = largesum(arr)
print(b)