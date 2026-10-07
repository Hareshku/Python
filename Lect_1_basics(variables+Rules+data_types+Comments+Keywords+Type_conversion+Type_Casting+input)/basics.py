# print("Hello")

# automatic type conversion is done in python 
# a="Hello "
# b="Haresh"
# print("first ",a+b) # Hello Haresh
# print(a,b)


# without type casting 
# a= 3
# b= "5"
# sum = a+b
# print(sum) # this will give error

# type casting 
# a= 3
# b= "5"
# sum = a+ int(b)
# print(a+ int(b)) #this will not give error

#  1 Write a Program to input 2 numbers & print their sum.

# num1= int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# print("Sum: ", num1+num2)

#  2 WAP to input side of a square & print its area

# side= int(input("Enter the side length of the square: "))
# area = side*side
# print("Area of the square is: ", area)

# 3 WAP to input 2 floating point numbers & print their average.
# num1 = float(input("Enter floating point one: "))
# num2 = float(input("Enter floating point two: "))

# average = (num1+num2)/2

# print("The avg of two floating point numbers is: ", average)

# 3 WAP to input 2 int numbers, a and b. 
# Print True if a is greater than or equal to b. If not print False.
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

if a>b:
    print("True")

else:
    print("False")


# str1= "Hello"
# str2= " World"
# str= str1+str2
# print(str,len(str))
# print(str[2:12])
# print(str[:-5])

# str='this is Python course'
# print("Number of occurance ",str.count("$"))
# print(str.replace("is", "in"))
# print(str.find("is"))
# print(str.endswith('ser'))

# print(value, end = " ") # to print result in one line
# print(value, sep=",") # to separate result value with specific character like , - _ etc.