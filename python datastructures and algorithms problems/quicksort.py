def quicksort(arr):
	quicksorthelper(arr,0,len(arr)-1)
	


def quicksorthelper(arr,first,last):

	if first<last:
		splitpoint = partition(arr, first, last)
		print('first value in quicksorthelper' , first,'and splitpoint' , splitpoint)
		print('first recursive call')
		quicksorthelper(arr, first , splitpoint-1)
		print(splitpoint)
		print('second recursive call')
		print(splitpoint)
		quicksorthelper(arr, splitpoint+1, last)

	

def partition(arr,first,last):
	pivotvalue = arr[first]
	leftmark = first+1
	rightmark = last


	done = False
	
	while not done:

		while leftmark <= rightmark and arr[leftmark]<=pivotvalue:
			
			leftmark += 1
		print('leftmark', leftmark)	

		while  arr[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark -= 1
		print('rightmark', rightmark)
	   

		if rightmark < leftmark:
			print('if is executed')
			done = True
		else:
			print('else is executed')
			temp = arr[leftmark]
			arr[leftmark] = arr[rightmark]
			arr[rightmark] = temp

	temp = arr[first]
	arr[first] = arr[rightmark]
	arr[rightmark] = temp
	print('right mark at the end',rightmark , 'and the first value is ', first)
	return rightmark


arr = [10,5,20,15]
quicksort(arr)


