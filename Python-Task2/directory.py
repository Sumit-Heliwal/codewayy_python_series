# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:00:25 2020

@author: Sumit
"""

#creating a dictionary:
languages = {1:"Java",2:"Python",3:"PHP",4:"HTML"}
print("The dictionary of language: ",languages)

get_language=languages.get(2) #using get() method
print(get_language)
keys = languages.keys() #using keys() method
print("keys: ",keys)
length = len(languages) #using length method
print(length)
values = languages.values() #using values()method
print(values)
items = languages.items() #using items() method
print(items)
languages.pop(4) #using pop() method
print(languages)
languages_new = languages.copy() #using copy() method
print(languages_new)
