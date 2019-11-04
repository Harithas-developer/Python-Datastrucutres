# def finder(arr1, arr2):
# 	arr1.sort()
# 	arr2.sort()

# 	for n1 , n2 in zip(arr1,arr2):
# 		if n1 != n2:
# 			return n1

# 	return arr1[-1]

# b = finder([4,5,3,2,1] ,[1,2,4,3])
# print(b) 


import collections 

def finder(n1,n2):
	d = collections.defaultdict(int)

	for num in n2:
		d[num] += 1
	print(d)

	for num in n1:
		if d[num] == 0:
			return num
		else:
			d[num] -= 1

a = [1,2,3]
b = [1,2]
c = finder([1,2,3] , [1,2])
print(c)