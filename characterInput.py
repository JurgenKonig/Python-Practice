def main():
	name = input("Please enter your name: ")
	age = input("Please enter your age: ")
	repeat_num = input("Please enter how many times you want the message to repeat: ")
	when_100 = 100 - int(age)
	for i in range(1, int(repeat_num), 1):
		print(str(i) + ". Your name is " + name + " and you are " + str(age) + " years old.")
		print("You will be 100 in " + str(when_100) + " years.")

main()
