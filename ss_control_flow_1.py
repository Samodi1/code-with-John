#Assignments
#Q1 Write a program that print all the odd numbers between variable A and Variable B

a = int(input("Enter first number:"))
b = int(input("Enter second number: "))

while a <= b:
    if a % 2:
        print(a)
    a += 1
    
# #Q2 Write a program giving a variable ss print all the even characters
ss = input("Enter string: ")
print(ss[1: :2])



