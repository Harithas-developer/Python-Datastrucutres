def merge(arr):
	if len(arr)>1:
		mid = len(arr)//2
		lefthalf = arr[:mid]
		righthalf = arr[mid:]
		
		merge(lefthalf)
		merge(righthalf)
		
		j = k = i =0
	

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k] = lefthalf[i]
				i+=1
			else:
				arr[k] = righthalf[j]
				j+=1
			k+=1
		print(arr)

		while i<len(lefthalf):
			arr[k] = lefthalf[i]
			i+=1
			k+=1

		while j < len(righthalf):
			arr[k] = righthalf[j]
			
			j+=1
			k+=1
	print('merge' , arr)
	
	

arr = [10,20,30,40]
merge(arr)