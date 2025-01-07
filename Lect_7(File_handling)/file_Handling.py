# import os 
with open("example.txt","r+") as f:
  # reads the entire file 
  data = f.read()  


  print(data)
#  reads the file line by line 
  f.readline()
  new_data= "Abc"

# # overwrites the entire file removes the existing data and then adds new data 
  f.write(new_data)
# os.remove("example.txt")

# Task 1: Create a new file “practice.txt” using python. Add the following data in it:
 
with open("Exercise.txt","x") as f:
  data= "Hi everyone\nwe are learning file I/O\nusing java\nI like programming in java"
  f.write(data)

# task 2: WAF that replace all occurrences of “java” with “python” in above file.

with open("Exercise.txt", "r") as f:
  data=f.read()
  new_data= data.replace("java", "Python")
  with open("Exercise.txt", "w") as f:
    f.write(new_data)

# task 3: Search if the word “learning” exists in the file or not.

with open("Exercise.txt", "r") as f:
  data=f.read()
  true=data.find("xlearning")
  if(true!=-1):
    print("found")
  else : print("Not found")

# task 4:  WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found.

def find_data():
 word= "learning"
 line_no=1
 data= True
 with open("Exercise.txt", "r") as f:
  while data:
   data=f.readline()
   if(word in data):
    print(line_no)
    return
   line_no+=1
 return -1
find_data()

# task 5: From a file containing numbers separated by comma, print the count of even numbers.

count=0
with open("demo.txt", "r") as f:
  data= f.read()
  nums= data.split(",")
  for val in nums:
    if(int(val) % 2==0):
      count+=1
  print(count)