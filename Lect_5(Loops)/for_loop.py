# list1= [36,49,64,81,100]
# for val in list1:
#   print(val)

# list1= [36,49,64,81,100]
# for val in range(len(list1)):
#   print(list1[val])

# list1= (1,4,9,16,25,36,49,64,81,100)
# x=81
# index=0
# for val in list1:
#   if(val==x):
#     print(val,"found at index ",index)
#     break
#   index+=1

# factorial through for loop
# num= int(input("Enter the number to find the factorial :"))
# i=num
# fact=1
# for i in range(num, 0, -1):
#   fact*=i
# print(fact)


 # Range function 
#  range(20):
#  range(1, 20):
# range(1, 20, 2) two is the steps
# range(20, 0, -1) to print in reverse order
# for i in range(10, 0, -1):
#   print(i)


num = int(input("Enter the number to find the factorial: "))
i =num
factorial=1
for i in range(num, 0, -1):
  factorial*=i

print(factorial)