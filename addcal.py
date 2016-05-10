#!/usr/bin/python


count = 0
total = 0
amount = int(input("how manynumbers do you want to add:"))
while count < amount:
    a = int(input("Number:"))
    total = total + a
    count = count + 1
print ("your sum is ",total)
