def add(num1, num2):
	return num1 + num2
	
def sub(num1, num2):
	return num1 - num2
	
def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2


def main():
	operation = input("What would you like to do (+,-,*,/):")
	if(operation == '+' or operation == '-' or operation == '*' or operation == '/'):
		var1 = int(input("Enter a number :"))
		if(type(var1) == int):
			var2 = int(input("Enter another number :"))
			if(type(var2) == int):
				if(operation == '+'):
					print (add(var1, var2))
				elif(operation == '-'):
					print (sub(var1, var2))
				elif(operation == '*'):
					print (mul(var1, var2))
				elif(operation == '/'):
					print (div(var1, var2))
				else:
					print ("not a valid input")
			else:
				print("Give a valid integer value")
		else:
			print("Give a valid integer value")
	else:
		print("Give a valid computation")
main()	