#!/usr/bin/python

count = 0
dif = 0
amount = int(input("Amount of numbers to be subtracted: "))
first = int(input("First Number: "))
while count < (amount - 1):
    a = int(input("Number:"))
    first = first - a
    count = count + 1
print("your result was",first)
