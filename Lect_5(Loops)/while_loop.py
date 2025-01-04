# task 1

# i= 1
# while i<=10:
#   print(i,"*",2,"=",i*2)
#   i+=1


# print("loop ended")

# task 2

# list1= [1,4,9,16,25,36,49,64,81,100]
# i=0
# while i< len(list1): 
#   print(list1[i])
#   i+=1


# list1= (1,4,9,16,25,36,49,64,81,100)
# i=0
# while i< len(list1): 
#   if(list1[i]==64):print("index = ",i,"Element = ",list1[i])
#   i+=1

# find the sum of first n numbers 
# i=0
# sum=0
# num=int(input("Enter the number any number to find the sum: "))
# while i<=num:
#   sum=sum+i
#   i+=1
# print(sum)

i=1
factorial=1
num=int(input("Enter the number any number to find the factorial: "))
while i<=num:
  factorial=factorial*i
  i+=1
print(factorial)