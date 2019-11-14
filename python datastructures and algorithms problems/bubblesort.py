def bubblesort(arr):
	for n in range(0, len(arr)-1 , 1):
		for k in range(n):
			if arr[k] < arr[k+1]:
				temp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = temp
	print(arr)

a =[ 22, 45, 36, 55, 17]
b = bubblesort(a)