class  MyClass:
    x = 5

p1 = MyClass()

print(p1.x)


#The __init__() method is used to assign values to object properties, or to perform operations that 
# are necessary when the object is being created.


class Person:
    def __init__(self, name, age=18, country="India"):
        self.name = name
        self.age = age
        self.country = country
    
p2 = Person("Omkar", 20)
p3 = Person(f"Ashley", country="Canada")

print(p2.name)
print(p2.age)
print(p2.country)
print(p3.name)
print(p3.age)
print(p3.country)




