def shellsort(arr):
	sublistcount= len(arr)//2
	while sublistcount > 0:
		for start in range(sublistcount):
			gap_insertion_sort(arr,start,sublistcount)
		sublistcount = sublistcount//2
	print(arr)

def gap_insertion_sort(arr,start,gap):
	for i in range(start+gap, len(arr) , gap):
		currentvalue = arr[i]
		position = i
		while position>=gap and arr[position-gap]>currentvalue:
			arr[position] = arr[position-gap]
			position = position-gap
		arr[position] = currentvalue


a = [10,23,5,7]
shellsort(a)