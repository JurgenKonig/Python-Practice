def main():
	num = int(input("Please enter a number: "))
	
	if (num % 2 == 0):
		print("Your number is even.")
	elif (num % 2 != 0):
		print("Your number is odd.")
	elif (num % 4 == 0):
		print("Your number is a multiple of 4.")
	
	num2 = int(input("Please enter another number to divide by: ")) 
	if (num / num2):
		print("Your numbers divide evenly.")
	else:
		print("Your numbers do not divide evenly.")

main()
