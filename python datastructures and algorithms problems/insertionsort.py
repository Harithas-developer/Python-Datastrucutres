def insertionsort(arr):
	for i in range(1,len(arr)):
		currentvalue = arr[i]
		print(currentvalue)
		position = i
		while position > 0 and arr[position-1]>currentvalue:
			arr[position] = arr[position-1]
			position = position-1
		arr[position] = currentvalue
		print(arr)


arr = [15,10,20,7]
insertionsort(arr)