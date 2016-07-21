#!/usr/bin/env python
#This program is to list out all the products of iphone variants and price
print ("Welcome to the world of iphone6")
print ("""Below are the available colors in iphone6
 Silver
 Grey
 Gold
 Pink""")

print ("Choose the color you would like to order")
color = raw_input(":")

if(color == "Silver"):
        print ("""Please choose the size from below list
        16GB
        64GB
        128GB""")
        size = raw_input(":")
        if(size == "16GB"):
				print ("Price is $600")
        elif(size == "64GB"):
                print ("price is $650")
        elif(size == "128GB"):
                print "price is $700"
        else:
                print ("Please enter the valid size available")
elif(color == "Grey"):
        print ("""Please choose the size from below list
        16GB
        64GB
        128GB""")
        size = raw_input(":")
        if(size == "16GB"):
                print "Price is $700"
        elif(size == "64GB"):
                print "price is $750"
        elif(size == "128GB"):
                print "price is $800"
        else:
                print ("Please enter the valid size available")

elif(color == "Gold"):
        print ("""Please choose the size from below list
        16GB
        64GB
        128GB""")
        size = raw_input(":")
        if(size == "16GB"):
                print "Price is $800"
        elif(size == "64GB"):
                print "price is $850"
        elif(size == "128GB"):
                print "price is $900"
        else:
                print ("Please enter the valid size available")

elif(color == "Pink"):
        print ("""Please choose the size from below list
        16GB
        64GB
        128GB"""0
        size = raw_input(":")
        if(size == "16GB"):
                print "Price is $900"
        elif(size == "64GB"):
                print "price is $950"
        elif(size == "128GB"):
                print "price is $1000"
        else:
                print ("Please enter the valid size available")

else:
        print ("This color not available")

