def sum_func(n):
    # Base case
    a = str(n)
    d = len(a)
    if d == 1:
        return n
    
    # Recursion
    else:
        return n%10 + sum_func(n/10)

c = sum_func(4321)
print(c)