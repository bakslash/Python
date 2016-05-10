#!/usr/bin/python

count = 0
amount = int(input("how many numbers you want to multiply: "))
b = int(input("First Number: "))
final = b
while count < (amount - 1):
    num = int(input("Number: "))
    final = final * num
    count = count + 1
print("your result was",final)
