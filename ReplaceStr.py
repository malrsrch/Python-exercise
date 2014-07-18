#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Here is am example for replace No. for str

number = '12345678'
dictReplace = {'1':'B','2':'r','3':'a','4':'v','5':'e','6':'l','7':'e','8':'e'}
#print dictReplace.items()

for item in dictReplace:
    #print item
    number = number.replace(item,dictReplace[item])

print number