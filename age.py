#!/usr/bin/env python
#this script is to tell when you will turn 100

import datetime
i = datetime.datetime.now()
thisyear=i.year
print ("please enter your name and age")
name = input("Please enter your name: ")
age = int(input("please enter your age: "))

rest=100-age
bal=rest+thisyear

print ("Hi %s you will turn hundred in the year %d" %(name,bal))