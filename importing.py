from math import sqrt

x = 2000
print("Rollin with Python: ", sqrt(400))

if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")

def squared(x):
    return x ** 2

def say_hi():
    print("Hi, this is module importing speaking.")

__version__ = "0.1"
