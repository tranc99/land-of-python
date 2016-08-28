class Person:
    def say_hi(self):
        print("Hello, my name is ", self.name)

    def __init__(self, name):
        self.name = name

p = Person("Swaroop")
p.say_hi()
