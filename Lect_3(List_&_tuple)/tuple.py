# tup1= (4,6,7,8,4,7)
# print(type(tup1))
# print(tup1[0:3])
# tup1[0]=9  // Not allowed in tuple
# print(tup1)
# print(tup1.index(6))
# print(tup1.count(4))

# task 1
#  WAP to count the number of students with the “A” grade in the following tuple.
#  [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
#  Store the above values in a list & sort them from “A” to “D”.
# grades= ("C", "D", "A", "A", "B", "B", "A")
# list1= list(grades)
# list1.sort()
# print(grades.count("A"))
# print(list1)

data = ([1,2,3], 10)

# data[0] = [4, 5]  x
# data.append(5)   x
data[0].append(4)
print(data)

a = (1, 3, 2)
b = (2, 2, 3)

print(a < b)

a = [1, 2, 3]
old_id = id(a)

a.append(4)

print(old_id == id(a))