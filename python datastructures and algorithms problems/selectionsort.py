def selectionsort(arr):
	for fillslot in range(len(arr)-1 , 0 , -1):
		positon_max = 0
		for location in range(1, fillslot+1):
			
			if arr[location] > arr[positon_max]:
				positon_max = location
		print(arr[fillslot])
		print(arr[positon_max])
		print(positon_max)
		temp  = arr[fillslot]
		arr[fillslot] = arr[positon_max]
		arr[positon_max] = temp
		print(arr)

a = [10,52,45,67,71]
selectionsort(a)