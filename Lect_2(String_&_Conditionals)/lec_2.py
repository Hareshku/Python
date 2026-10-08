# What is String 
# A string is a sequence of characters enclosed inside quotes.

# single, double, triple quotes
# s = "Hello"
# s1= 'Hello'
# s2 = """Hello"""

# S3 = "I'm"
# s4= '"Hello"'
# s5= """this is used for paragraph


# text"""
# print(s,s1, s2, s4, S3,s5)

# String can contain anything 
# text = "Python 🐍"

# To check Type of the variable: type()
# a = 33343
# b = "43434"

# String python treats as sequence of individual characters 
# word = "Python"
# print(word[0]) #p
# print(word[-1]) #n
# print(type(a))
# print(type(b))

# We use + sign to concatenate string in python 
# f_name= "Haresh"
# L_name= "Meghwar"

# full_name = f_name+ " "+ L_name

# print(full_name)


# How to repeat string 
# a = "="
# print(a*5)


# How to check if a specific character is present in string 

# word = "Python"
# print("Py" in word)
# print("Ja" not in word)
# print(word*4)

# text = "Python Programming"

# print("Python" in text)
# print("Java" in text)
# print("Java" not in text)
# print(repr(text[6])) # how to make invisible character visible


# indexing and slicing, indexing returns one character and slicing returns multiple characters 
# text = "Python"
# text[0] #P
# text[2: 5] #thon

# this will print characters and index 
# word = "Python"
# for i in range(len(word)):
#     print(i, word[i])


# String slicing (start:stop:step)
# stop position is excluded

text = "Python"

text[0:3]     # 'Pyt'
text[2:5]     # 'tho'
text[:3]      # 'Pyt'
text[3:]      # 'hon'
text[:]       # 'Python'
text[::2]     # 'Pto' for even position
text[1::2]    # 'yhn' for odd position
text[::-1]    # 'nohtyP'


# Two ways of concatenating the string 

# using + operator or using join fuction
# word = ['Python', 'is', 'easy']
# print(word[0]+" "+word[1]+" "+word[2])
# print(" ".join(word))

# # only prints the characters 
# for i in word:
#     print(i)

# String methods
# text = " Python programing "
# print(text.lower())
# print(text.upper())
# print(text.capitalize())
# print(text.title())
# print(text.find("P"))
# print(text.rfind("h"))
# print(text.index("o")) # same as find but give error if character is not present, while find gives -1
# print(text.count("p")) 
# print(text.startswith("p")) 
# print(text.endswith("g")) 
# print(text.replace("p", "G")) 
# print(text)
# print(text.split(" ")) 
# print(text.strip()) 


# word ='Python'

# print(word[::-1])
# print("".join(reversed(word)))

# word ='madam'
# revers= word[::-1]
# if revers==word:
#     print("paliandrom")


vowels= "Umbrella opinion"
count =0
vN= " "
for i in range(len(vowels)):
    if "a"==vowels[i] or "e"==vowels[i] or "i"==vowels[i] or "o"==vowels[i] or "u"==vowels[i].lower():
        count+=1
        vowels[i].join(vN)
print(count, vN)
# Task 1 
# name= input("Enter your name here:  ")
# print(name, " ",len(name))
# # message = "I'm learning Python"
# message = 'I\'m learning Python'
# print(message)
# task 2
# marks= int(input("Enter your marks here :  "))
# if(marks>=91 and marks<=100):print("Grade - A+")

# elif(marks>=83 and marks<=90):print("Grade - A")
# elif(marks>=75 and marks<=82): print("Grade - B+")
# elif(marks >=68 and marks<=74): print("Grade - B")
# else: print("fail")

# task 3
# num=int(input("Enter number : "))
# if(num%2==0):print(num," : is an even number")
# else: print(num, " : is odd number")

# task 4

# num1= int(input("Enter 1st number :  "))
# num2= int(input("Enter 2nd number :  "))
# num3= int(input("Enter 3rd number :  "))
# if(num1>num2 and num2>num3): print(num1, " is greater")
# elif(num2>num1 and num1>num3): print(num2, " is greater")
# elif(num3>num2 and num2>num1): print(num3, " is greater ")


# task 5 
# num= int(input("Enter 1st number :  "))
# if(num%7== 0): print(num, "Number is multiple of 7")
