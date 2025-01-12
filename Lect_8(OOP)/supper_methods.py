# Super keyword to access attributes of the parent class 

class Car:
  def __init__(self, type):
    self.type=type
  @staticmethod
  def start():
    print("Car started....")

  @staticmethod
  def stop():
    print("Car stoped...")

class ToyotaCar(Car):
  def __init__(self, name, type):
    super().__init__(type)
    self.name=name


c1=ToyotaCar("BMW","asdf")

c1.start()
print(c1.type)