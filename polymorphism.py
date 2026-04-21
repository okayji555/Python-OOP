class vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Move!")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("Sail!")

car1 = car("Masserati")
boat1 = boat("Yacht")

for x in (car1, boat1):
    print(x.name)
    x.move()