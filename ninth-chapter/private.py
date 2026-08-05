class Person:
    name = "anonymous"

    def __hello(self): 
        return f"Hello, my name is {self.name}"

    def greeting(self):
        return self.__hello()

p1 = Person()
print(p1.name)

print(p1.greeting())

class Person:
    def __init__(self, name):
        self.__name = name

p1 = Person("Alice")

print(p1.__name)