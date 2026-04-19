
"""
The self parameter is a reference to the current instance of the class.
It is used to access properties and methods that belong to the class.
"""
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emily", 23)

p1.greet()




#another example

class carInfo:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def displayInfo(self):
        print(f"{self.brand}, {self.model}, {self.year}")

car1 = carInfo("Masserati", "Luxury1", 2027)
car1.displayInfo()

"""
#calling one method from another method
"""
class website:
    def __init__(self, name):
        self.name = name    

    def greet(self):
        return "Hello! " + self.name
    
    def greet2(self):
        message = self.greet()
        print(message + " Welcome to the website!")

p1 = website("Ajraj")
p1.greet2()
"""

name = input("What's your name: ")
print("Hello! " + name + " welcome to omkar's life")