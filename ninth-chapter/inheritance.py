class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")


    @staticmethod
    def stop():
        print("Car stopped")

class ToyatoCar(Car):
    def __init__(self , name ):
        self.name = name

car1 = ToyatoCar("Frtuner")
car2 = ToyatoCar("pirus")

print(car1.start())
print(car1.color)


     