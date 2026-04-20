class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def display(self):
            print("this is inner class")
                

outer = Outer()
print(outer.name)
inner = Outer.inner()
inner.display()

#example

class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()