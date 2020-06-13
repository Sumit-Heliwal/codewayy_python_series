# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:27:07 2020

@author: Sumit
"""

#creating a tuple:
rollno = (1,2,3,4,5,6,10,15)
print("The tuple of rollno : ",rollno)
rollno_3= rollno[:3] #sub tupple method
print(rollno_3)
index = rollno.index(10) #using index() method
print("The index of 10 is: ",index)
length = len(rollno) #using length() method
print("The length of the rollno tuple is: ",length)
maximum_roll_no = max(rollno) #using max() method
print("The maximum roll_no : ",maximum_roll_no)
minimum_roll_no = min(rollno) #using min() method
print("The minimum roll_no : ",minimum_roll_no)
Sum =sum (rollno) #using sum() method
print("The sum of all elements in the tuple rollno is: ",Sum)
list = [1,2,3,4] 
Tuple = tuple(list) #conversion of list to tuple
print("The tuple obtained by converting a list into tuple is: ",Tuple)
