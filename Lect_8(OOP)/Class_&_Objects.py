# class Students:
#   # we use class attribute when something is common in multiple thnings
#   College_Name="XYZ"
#   # Default constructor allways executed when object of the class is created 
#   def __init__(self):
#     print("This is default constructor executed by default.")
  
#   # parameterized constructor 
#   # inside the constructor the attributes are called "object attribute" 
#   def __init__(self, name, marks):
#     self.name=name
#     self.marks=marks

# s1=Students('Kumar', 68)
# print("Student name : ",s1.name,"\nMarks : ",s1.marks, "\nCollege Name : ", s1.College_Name)

# # del Keyword 
# class Students:
#   def __init__(self, account, password):
#     self.account=account
#     self.password=password
  
#   def hello(self):
#     print("Hello account holder! ")

# acc1= Students(38383, 1234)
# acc1.hello()
# del acc1 # this delete the object instance and release the memory location occupaied by variable
# print(acc1)

# public and private variable and methods 

class Students:
  def __init__(self, account, password):
    self.account= account # public variable
    self.__password= password # this is private variable can only be accessed inside the class we use this when we want to keep confidential information safe.
  
  # method can also be made private
  def __welCom(self):
    print("welcome")

  def hello(self):
    self.__welCom()
    print("Hello user this is your password : ",self.__password)

acc1= Students(344343, 12345)
print(acc1.account)
acc1.hello()
