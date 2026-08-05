#Single inheritance

class School:
    medium = "English"

    @staticmethod
    def open():
        print("School is open")

    @staticmethod
    def close():
        print("School is closed")


class CSV(School):
    def __init__(self, review):
        self.review = review


s1 = CSV("Good")     # Create a CSV object
print(s1.review)
s1.open()

# 2 Multilevel inheritance

class Car():
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyatoCar(Car):
    def __init__(self , brand):
        self.brand = brand

class Fortuner(ToyatoCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1 = ToyatoCar("Fortuner")
car1.start()
car1.stop()

Multiple inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome t class C"

c1 = C()

print(c1.varA)
print(c1.varC)
print(c1.varB)



    
