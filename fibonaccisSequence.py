def main():
	num = 1
	a = []
	iterations = int(input("Please enter the number of places in Fibonacci's Sequence you'd like to populate the list with: ")
	for i in range(0, iterations, 1):
		a.append(num)
		if (i < 1):
			num *= 1
		else:
			num = a[i] + a[i - 1]
	print("Completed list: " + str(a))
	
	b = []
	num = int(input("Please enter a number to compare to the list: "))
	for i in range(0, len(a), 1):
		if (a[i] < num):
			c.append(b[i])
	print("Numbers less than " + str(num) + ": " + str(b))	
main()
