def main():
	num = 1
	a = []
	for i in range(0, 20, 1):
		a.append(num)
		if (i < 1):
			num *= 1
		else:
			num = a[i] + a[i - 1]
	print("Completed list: " + str(a))
	
	b = []
	for i in range(0, len(a), 1):
		if (a[i] < 5):
			b.append(a[i])	
	print("Numbers less than 5: " + str(b))
	
	c = []
	num = int(input("Please enter a number to compare to the list: "))
	for i in range(0, len(a), 1):
		if (a[i] < num):
			c.append(a[i])
	print("Numbers less than " + str(num) + ": " + str(c))	
main()
