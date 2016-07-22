def helloworld(myString):
	print(myString)
	myName = input("what is your name?")
	myVar = input("Enter a number: ")
	myVar2 = input("Enter another number :")
	if((myName == "santosh" and myVar == "0") or myVar2 == "5"):
	    print("santosh is great")
	elif(myName == "raghu"):
	    print("you are cool")
	else:
	    print("No one is good")

helloworld("This is first set of calling code")
helloworld("This is second set of calling code")