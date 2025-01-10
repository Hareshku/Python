# class Students:
#   def __init__(self,name, mark):
#     self.name= name
#     self.marks=mark
#     print("this is default constructor ")
  
#   def hello(self):
#     print("this is methods hello", self.name)
  
#   def getMarks(self):
#     return self.marks

# s1= Students("Haresh", 98)
# s1.hello()
# print("Marks : ",s1.getMarks())


# Task 1
# class Students:
#   def __init__(self, name, marks):
#     self.name= name
#     self.marks= marks
#   def Avg(self):
#     sum=0
#     for val in self.marks:
#       sum+=val
#     print(self.name, "your avg mark is :", sum/3)
  
# s1= Students("Haresh", [79, 95, 93])
# s1.Avg()

# Static methods

# class Students:
#   @staticmethod   #Decorator this allows you to make your method static 
#   def welCom():
#     print("Welcom coders.")

# s1= Students()
# s1.welCom()