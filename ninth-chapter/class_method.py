class Person:
    name = "anonymous"

    # def changename(self, name):
    #    self.__class__.name = name

    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person()
print(p1.name)

p2 = Person()
p2.changename("Neeharika")
print(p2.name)
