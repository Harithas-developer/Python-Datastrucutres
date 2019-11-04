# def fibo(n):
# 	if n == 0 or n==1:
# 		return n
# 	else:
# 		return fibo(n-1)+fibo(n-2)

# b = fibo(10)
# print(b)

# using Memonization
n =10
cache = [None]*(n+1)

def fibo(n):
	if n==0 or n==1:
		return n

	if cache[n] != None:
		return cache[n]

	cache[n] = fibo(n-1) + fibo(n-2)
	
	return cache[n]

b = fibo(10)
print(b   )