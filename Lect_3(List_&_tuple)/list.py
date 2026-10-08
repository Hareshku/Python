marks= [94, 89, 87, 78, 60, 9, 23, 40, 60]
# marks[0]="list"
# marks[2]="type"
# marks.append("add-one")
marks.sort()
# remove(30)\
# print(marks.pop(8))
# marks.sort(reverse=True)
# print(marks)
# marks.reverse()
# print(marks)
# marks.insert(2, 99)
# print(marks)
# marks.remove(89)  #removes the elements of list

# # print(marks.pop(3)) by defaul delete last element but if we want to delete a specific element then it takes index of the element


# print(marks[-6:-1]) #ending index is excluded
# # print(len(marks))
# print(marks)
# print(list(range(6)))

# if 69 in marks:
#     print("60 is present: ")
# else: print("Not present")

# find the index of a given value 
# print(marks.index(60, 2))
# print(marks.count(60))

word = "programming"
for char in word:
    print(word.count(char))
# # task 1
# # WAP to ask the user to enter names of their 3 favorite movies & store them in a list

# # fav_List= []
# # movie1 = input("Enter 1st movie :  ")
# # fav_List.append(movie1)
# # movie2 = input("Enter 2nd movie :  ")
# # fav_List.append(movie2)
# # movie3 = input("Enter 3rd movie :  ")
# # fav_List.append(movie3)

# # print(fav_List)

# # task 2
# # WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# #  [1, 2, 3, 2, 1]
# #  [1, “abc”, “abc”, 1]


# # list1= [1,2,3,2,8]
# # list2=[]
# # list2=list1.copy()
# # list2.reverse()

# # if(list1==list2): print("it a palindrome")
# # else: print("not palindrome")
# # print(list1)
# # print(list2)



# # Python List Operations

# # 1. len()
# Definition: Returns the total number of elements in a list.

# Syntax
# len(list_name)

# # 2. Negative Indexing
# Definition: Negative indexing allows you to access elements from the end of the list.

# -1 → Last element
# -2 → Second last element
# -3 → Third last element

# Example
# numbers = [10, 20, 30, 40, 50]

# print(numbers[-1]) 
# print(numbers[-2])

# # 3. append()
# Definition: Adds a single element to the end of the list.

# Syntax
# list.append(item)



# # 4. extend()
# Definition: Adds all elements of another iterable (list, tuple, etc.) to the end of the list.

# Example
# numbers = [1, 2]

# numbers.extend([3, 4, 5])    #[1, 2, 3, 4, 5]


# # 5. insert()
# Definition: Inserts an element at a specified index.

# Example
# numbers = [10, 20, 40]
# numbers.insert(2, 30)   #[10, 20, 30, 40]

# # 6. remove()
# Definition: Removes the first occurrence of the specified value.

# Example
# numbers = [10, 20, 30, 20]

# numbers.remove(20)  #[10, 30, 20]


# # 7. pop()
# Definition: Removes and returns the element at the specified index. If no index is given, it removes the last element.

# Example
# numbers = [10, 20, 30]
# removed = numbers.pop()    #[10, 20]


# # 8. clear()
# Definition: Removes all elements from the list.

# Example
# numbers = [1, 2, 3]
# numbers.clear()   #[]


# # 9. min()
# Definition:  Returns the smallest element in the list.

# Example
# numbers = [45, 10, 70, 2]
# print(min(numbers))  #2



# # 10. max()
# Definition: Returns the largest element in the list.

# Example
# numbers = [45, 10, 70, 2]
# print(max(numbers))   #70


# # 11. Slicing
# Definition: Extracts a portion of the list.

# Syntax
# list[start:end:step]
# start → Included
# end → Excluded
# step → Optional

# Example
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])  #[20, 30, 40]


# print(numbers[::-1])    #[50, 40, 30, 20, 10]



# # 12. count()
# Definition:  Returns how many times a value appears in the list.

# Example
# numbers = [10, 20, 10, 30, 10]  
# print(numbers.count(10)) #3



# # 13. sort()
# Definition: Sorts the list in ascending order by default.

# Example
# numbers = [40, 10, 30, 20]
# numbers.sort()  #[10, 20, 30, 40]

# Descending:

# numbers.sort(reverse=True)  #[40, 30, 20, 10]


# # 14. reverse()
# Definition: Reverses the order of the list.

# Example
# numbers = [10, 20, 30]
# numbers.reverse()   #[30, 20, 10]


# # 15. copy()

# # difference between copy and =
# # copy just copy elements 
# # while = assign same address to another variable
# Definition:  Creates a shallow copy of the list.

# Example
# numbers = [1, 2, 3]
# copy_numbers = numbers.copy()  #[1, 2, 3]


# # 16. index()
# Definition:  Returns the index of the first occurrence of a value.

# Example
# fruits = ["Apple", "Banana", "Mango"]

# print(fruits.index("Banana"))  #1