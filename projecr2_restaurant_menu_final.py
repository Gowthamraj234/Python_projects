# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:48:10 2024

@author: GOWTHAMRAJ P R
"""


from collections import Counter

print("welcome to italiano")
print('''1.pizza:\trs.150
2.burger:\trs.135
3.pasta:\trs.175''')

menu = {'pizza':150,'burger':135,'pasta':175}

items = input("Enter the items purchased (separated by space): ").split(',')
list1 = []

print("Items purchased:")

for thing in items:
    list1.append(thing)
    
print(list1)

item_counts = Counter(list1)

total = 0

for item,price in menu.items():
    if item in list1:
        total+=price*item_counts[item]
else:
    for jar in list1:
        if jar not in menu:
            print(jar)
    print("the entered object is not avaiable")


print(item_counts)        

print("the total amount for the items purchased : ",total)
        
    








































