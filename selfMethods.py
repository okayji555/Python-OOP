class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = person("ladoo", 19)
print(p1)


#multiple methods

class Cars:
    def __init__(self, name):
        self.name = name
        self.favcar = []

    def add_car(self, CarName):
        self.favcar.append(CarName)
        print(f"Added: {CarName}")

    def remove_car(self, CarName):
        if CarName in self.favcar:
            self.favcar.remove(CarName)
            print(f"Removed: {CarName}")

    def show_car(self):
        print(f"Cars: {self.name}")
        for CarNames in self.favcar:
            print(f"- {CarNames}")


my_car_collection = Cars("Favorites")
my_car_collection.add_car("Masserati")
my_car_collection.add_car("Mercedes")
my_car_collection.add_car("BMW")
my_car_collection.add_car("Honda")
my_car_collection.remove_car("Honda")
my_car_collection.show_car()     