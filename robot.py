class Robot:
    """Represents a robot, with a name."""
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed! ".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last robot ".format(self.name))
        else:
            print("There are still {:d} robots working ".format(Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {} ".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots ".format(cls.population))

droid1 = Robot("R2-D2")
droid2 = Robot("T800")

droid1.say_hi()
Robot.how_many()
droid1.die()
Robot.how_many()
