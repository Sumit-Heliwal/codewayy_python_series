# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:17:10 2020

@author: Sumit
"""

#creating a set:
languages = {"Java","Python","PHP","HTML"}
print("The set of languages : ",languages)
languages.add("CSS") #using add() method
print("languages set after adding",languages)
languages.update(["JS","Kortlin"]) #using update() method
print("set after updation: ",languages)
length = len(languages) #using length() method
print("The length of the languages set is: ",length)
languages.remove("CSS") #using remove() method
print("The languages set after removing ",languages)
languages.discard("HTML") #using discard() method
print("The languages set after discarding ",languages)
languages.pop() #using pop() method
print("The languages set after performing a pop opearation: ",languages)
languages.clear() #using clear() method
print("The set languages after using clear method: ",languages)