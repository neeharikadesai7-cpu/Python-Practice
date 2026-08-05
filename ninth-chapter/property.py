class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def avg(self):
        return str((self.phy + self.chem + self.math) / 3 )+ "%"


s1 =Student(100, 90, 80)
print(s1.avg)

s1.math = 100
print(s1.avg)