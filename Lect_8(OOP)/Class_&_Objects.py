class Students:
  # we use class attribute when something is common in multiple thnings
  College_Name="XYZ"
  # Default constructor allways executed when object of the class is created 
  def __init__(self):
    print("This is default constructor executed by default.")
  
  # parameterized constructor 
  # inside the constructor the attributes are called "object attribute" 
  def __init__(self, name, marks):
    self.name=name
    self.marks=marks

s1=Students('Kumar', 68)
print("Student name : ",s1.name,"\nMarks : ",s1.marks, "\nCollege Name : ", s1.College_Name)
# print("Student name : ",s1.s_Name,"Marks : ", s1.marks)