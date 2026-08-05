class Complex:
    def __init__(self,real,complex):
        self.real = real
        self.complex = complex

    def shownumber(self):
        print(self.real, "i" + "+", self.complex, "j")

    # def add(self, num2):
    #     newreal = self.real +num2.real
    #     newcomplex = self.complex + num2.complex
    #     return Complex(newreal , newcomplex)


#dunder function are also called magic function or special fumctions

    def __add__(self, num2):
            newreal = self.real + num2.real
            newcomplex = self.complex + num2.complex
            return Complex(newreal , newcomplex)

    def __sub__(self, num2):
                newreal = self.real - num2.real
                newcomplex = self.complex - num2.complex
                return Complex(newreal , newcomplex)
    
num1 = Complex(1,2)
num1.shownumber()

num2 = Complex(7,5)
num2.shownumber()

# num3 = num1.add(num2)
# num3.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()