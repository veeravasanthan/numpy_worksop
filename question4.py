#write a program to find the sum of digits of a given number'
def getSum(n): 
	
	sum = 0
	for digit in str(n): 
	sum += int(digit)	 
	return sum

n = 12345
print(getSum(n))
