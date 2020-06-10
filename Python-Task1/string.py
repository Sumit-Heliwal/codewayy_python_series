# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:36:36 2020

@author: Sumit
"""

#Full Name( String concatenation should be used)
fname=input("first name")
lname=input("last name")
print("fullname ",fname,lname)
#College name with address (Use string concatenation)
cname=input("college name")
add=input("address")
print("{}{}".format(cname,add))
#Initialize marks of  5 different subjects with good variable names.
python = int(input("marks of python"))
java = int(input("marks of java"))
cs = int(input("marks of cs"))
js = int(input("marks of js"))
php = int(input("marks of php"))

#Calculate and display the total marks, percentage.
total = python+java+cs+js+php
print("total marks = ",total)
print("percentage = ",total/5)