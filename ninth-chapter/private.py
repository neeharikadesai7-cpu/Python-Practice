class Person:
    name = "anonymous"

p1 = Person()

print(p1.name)


class Person:
    __name = "anonymous"

p1 = Person()

print(p1.__name)