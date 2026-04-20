class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age   #this has become a private property

  def get_age(self):
    return self.__age       #to access the private property

p1 = Person("Tobias", 25)
print(p1.get_age())

