class student:
    college_name = "DYPCET"

    def __init__(self,fullname):
        self.name = fullname
        print("Adding new student to database")

s1 = student("Karan")
print(s1.name)

s2 = student("Neeharika")
print(s2.name)

s3 = student("Virat")
print(s3.name)

print(s1.college_name)
print(s2.college_name)
print(s3.college_name)
