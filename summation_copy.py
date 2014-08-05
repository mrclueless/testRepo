def summation(a,b):
	sum = 0
	for n in range(a,b+1):
		sum = sum + n
	return sum

a = summation(1,100)
b = summation(1,200)
print a
