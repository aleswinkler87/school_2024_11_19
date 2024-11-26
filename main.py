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
"""
class passport:
    def __init__(self, citizen):
        self.citizen = citizen
    def makeprint1(self):
        print(f"I am from {self.citizen}")

class foreignpassport(passport):
    def __init__(self, citizen, visas):
        passport.__init__(self, citizen)
        self.visas = visas
    def makeprint2(self):
        print(f"I want to visit {self.visas}")

f1 = foreignpassport("czech", "USA")


f1.makeprint1()
f1.makeprint2()
"""
"""class Num:
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other.n

    def __add__(self, other):
        if type(other) is Num:
            return Num(self.n + other.n)
        return  Num(self.n + other)

    def __str__(self):
        return f"{self.n}""""

"""n1 = Num(1)
n2 = Num(1)
print(n1)
print(n2)
n3 = n1
print(n1 == n2)
print(n1 == n3)

n4 = n1 + n2
print(n4)


def add(a, b):
    return a + b

print(add(5, 6))
print(add(Num(10), Num(20)))
print(add(Num(10), 5))
"""
"""
1/2  1/3

x/6

3/6   2/6

5/6
"""


class zlomek:
    def __init__(self, citatel, jmenovatel):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

    def __add__(self, other):
        # Addition of two fractions
        citatel = self.citatel * other.jmenovatel + other.citatel * self.jmenovatel
        jmenovatel = self.jmenovatel * other.jmenovatel
        return zlomek(citatel, jmenovatel)