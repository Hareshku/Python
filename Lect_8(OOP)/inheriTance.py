# Single level Inheritance 

# class Car:
#   @staticmethod
#   def start():
#     print("Car started....")

#   @staticmethod
#   def stop():
#     print("Car stoped...")

# class ToyotaCar(Car):
#   def __init__(self, name):
#     self.name=name
#   model="2025"


# c1=ToyotaCar("BMW")

# c1.start()

# # Multi-Level Inheritance 
# class Car:
#   @staticmethod
#   def start():
#     print("Car started....")

#   @staticmethod
#   def stop():
#     print("Car stoped...")

# class ToyotaCar(Car):
#   def __init__(self, name):
#     self.name=name
#   model="2025"

# class Mehran(ToyotaCar):
#   def __init__(self,color):
#     self.color=color

# c1=Mehran("White")

# c1.start()

# Multiple Inheritance 
class Car:
  @staticmethod
  def start():
    print("Car started....")


class ToyotaCar():
  @staticmethod
  def stop():
    print("Car stoped...")

class Cars(Car, ToyotaCar):
  print("dfsdfs")

c1=Cars()

c1.start()
c1.stop()