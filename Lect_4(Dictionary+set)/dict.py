# info={
#   "name": "Haresh",
#   "last_Name": "Kumar",
#   "marks": [2,3,4,5,6],
# }

# marks=info['marks'][0]
# print(info['name'],info['last_Name'], marks, info['marks'])
# info['name']="Hareesh"
# info['surname']="Meghwar"
# print(info)

# Nested dictionary 
# student={
#   "name":"Haresh",
#   "subj": {
#   "Eng":92,
#   "Java": 93,
#   "C++": 94,
#   },
#   "Teacher": "xyz",
# }

# print(student["subj"]["Java"])


# dictionary methods

# print(student.keys())
# print(list(student.keys()))
# print(list(student.items()))
# print("before")
# print(student.get("sname"))
# print(student["sname"])
# print("After")

# new_stu={"City": "Hyderabad", "Country": "Pakistan", "Province":"Sindh"}
# student.update(new_stu)
# print(student)


# Exercise 
# task1={"table":{"a piece of furniture", "list of facts and figures"}, "cat":"a small animal"}
# print(task1["table"],task1["cat"])

# task2 ={"Python":"3","Java":"3", "C++":"2", "C":"1", "Javascript":"1", }

# Task 3
subjects= {}
subj_1=float(input("Enter the 1st subject marks :  "))
subj_2=float(input("Enter the 2nd subject marks :  "))
subj_3=float(input("Enter the 3rd subject marks :  "))

subjects.update({"Java":subj_1, "C++":subj_2, "Python":subj_3})
# print(type(subjects))
print(subjects["Java"])