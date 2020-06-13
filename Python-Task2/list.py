# -*- coding utf-8 -*-
"""
Created on Sat Jun 13 090025 2020

@author Sumit
"""

#creating a list
rollno = [1,2,3,4,5,6,10,15]
print("The list of rollno  ",rollno)
rollno.append(20) #using append() method
print("The list of rollno ",rollno)
rollno.insert(6,7) #using insert() method
print("The list of rollno ",rollno)
rollno.remove(15) #using remove() method
print("The list of rollno ",rollno)
rollno.pop() #using pop() method
print("The list of rollno ",rollno)
rollno.extend([22,25,28])  #using extend() method
print("The list of rollno ",rollno)
min_rollno = min(rollno) #using min() method
print("The minimum number from the list of rollno is ",min_rollno)
max_rollno = max(rollno) #using max() method
print("The max of all elements in the list of rollno is ",max_rollno)
