class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Development", 700000)

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
        super().show_details()

        
eng1 = Engineer("Neeharika", 18)
eng1.show_details()
