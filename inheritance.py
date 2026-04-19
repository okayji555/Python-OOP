class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, amount):
        self.health -= amount

class Warrior(Character):  #this is inheritance, where warrior class is child of Character class
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)

#here the super() calls the parent class init method and passing the variables to the warrior(child class)    


warrior = Warrior(100, 50, 10)
print(f"Intial Health: {warrior.health}")
warrior.take_damage(40)
print(f"Health after damage: {warrior.health}")