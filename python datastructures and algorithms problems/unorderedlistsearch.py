def search(arr, elem):
	pos = 0
	found = False
	stopped = False

	while pos < len(arr) and not found:
		if arr[pos] == elem:
			found = True 
		else:
			if arr[pos] > elem:
				stopped = True
			else:
				pos +=1
	return found

arr = [1,2,3,4]
elem = 5

a = search(arr, elem)
print(a)
