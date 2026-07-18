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

#2 

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
        
    


    
