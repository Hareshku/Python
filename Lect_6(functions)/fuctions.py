#  Functions are the Block of statements that perform a specific task.
# if we have to perform addition at multiple time then it increase the line of code due to this redundancy also increase this is not a good programming approach so we use functions that reduce the line of code along with redundancy

# a= 2
# b=5
# sum=a+b
# print("Sum = ",sum)



# # function
# def sum(a,b):
#   sum=a+b
#   print("sum = ",sum)
#   # return sum

# sum(4,5)
# sum(10,30)
# sum(40,39)


# def Multiply(a,b,c):
#   mul=a*b*c
#   print("multiple of three numbers = ",mul)

# Multiply(3,4,7)


# # WAP to calculate the avg of three numbers 
# def avg(a,b,c):
#   avg= (a+b+c)/3
#   print('avg = ',avg)

# avg(2,5,8)


# default parameters

# def sum(a=1,b=2):
#   sum=a+b
#   print("sum = ",sum)
# sum()


# #  Task 1: WAF to print the length of a list. ( list is the parameter)
# list1= [1,2,3,4,5]
# def lengtH(listt):
#   print("length of the list is =",len(listt))

# lengtH(list1)
# #  Task 2: WAF to print the elements of a list in a single line. ( list is the parameter)
# list1= [9,4,3,4,5]
# def lengtH(listt):
#   i=0 
#   print("list in one row  = ", end=" ")
#   for i in range(len(listt)):
#     print(listt[i], end=",")
#   print()
# lengtH(list1)

# #  Task 3: WAF to find the factorial of n. (n is the parameter)
# num =int(input("Enter the number to find the factorial : "))
# def factorial(num):
#   fact =1
#   i=1
#   while i<=num:
#     fact*=i
#     i+=1
#   print("Factorial of n = ",num," is =",fact)

# factorial(num)
# # Task 4:  WAF to convert USD to PKR.
# usd= int(input("Enter USD to convert into pkr : "))
# def USD_to_PKR(usd):
#   pkr=usd*278
#   print(usd,"USD =",pkr,"PKR")

# USD_to_PKR(usd)


# take a number input from the user and check if the input number is odd then return odd string else return even string

# num= int(input("Enter the number to check wether the given number is odd or even : "))
# def odd_Even(num):
#   if(num%2==0):
#     print(num," is a even number")
#   else: 
#     print(num," is a odd number")

# odd_Even(num)


# Recursion
# function call itself

def Show(n):
  if(n==0):
    return
  print(n)
  Show(n-1)
Show(5)