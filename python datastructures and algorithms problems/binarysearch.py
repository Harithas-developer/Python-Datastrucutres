# def binarysearch(arr, elm):

# 	first = 0
# 	last = len(arr)-1
# 	found = False

# 	while first <= last and not found:
# 		mid = (first+last)//2
		
# 		if arr[mid] == elm:
# 			found = True
# 		else:
# 			if elm < arr[mid]:
# 				last = mid-1
# 			else:
# 				first = mid+1
# 	return found

# arr = [22,34,55,66,78]
# elm = 78

# a = binarysearch(arr, elm)
# print(a)


def recursive(arr, elm):
	if len(arr) ==0:
		return False
	else:
		mid = len(arr)//2
		if arr[mid] == elm:
			return True
		else:
			if elm < arr[mid]:
				return recursive(arr[:mid-1],elm)
			else:
				return recursive(arr[mid+1:],elm)

arr = [1,2,3,4,5,6,7,8,9,10]
elm = 11
a = recursive(arr,elm)
print(a)