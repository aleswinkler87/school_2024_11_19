print("fff")
"""
class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")

class Worker(Human):
    def __init__(self, name, position):
        Human.__init__(self, name)
        self.position = position

    def say_position(self):
        print(f"I work like a {self.position}")

w1 = Worker("john", "teacher")

w1.say_hello()
w1.say_position()

"""

class passport:
    def __init__(self, citizen):
        self.citizen = citizen

class foreignpassport:
    def foreignpassport(passport):